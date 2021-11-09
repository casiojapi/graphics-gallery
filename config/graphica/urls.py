
from django.urls import path

from .views import (
    ImageListView,
    ImageTagListView,
    ImageDetailView,
    ImageCreateView,
    ImageUpdateView,
    ImageDeleteView
)

app_name = 'image'

urlpatterns = [

    path('', ImageListView.as_view(), name='list'),

    path('tag/<slug:tag>/', ImageTagListView.as_view(), name='tag'),

    path('image/<int:pk>/', ImageDetailView.as_view(), name='detail'),

    path('image/create/', ImageCreateView.as_view(), name='create'),

    path('image/<int:pk>/update/', ImageUpdateView.as_view(), name='update'),

    path('image/<int:pk>/delete/', ImageDeleteView.as_view(), name='delete'),
]
