from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model



class Image(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title


