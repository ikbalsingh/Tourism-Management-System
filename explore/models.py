from django.db import models
from authen.models import Profile


# Create your models here.
class Flyer(models.Model):
    creater = models.ForeignKey(Profile)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    photos = models.ImageField(blank=True, null=True)

    def __str__(self):
      return self.title+","+self.description+","+self.location
    