from django.db import models
from authen.models import Profile


# Create your models here.
class Flyer(models.Model):
    creater = models.ForeignKey(Profile)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
      return self.title + "," + self.description + "," + self.location


class Photo(models.Model):
	user = models.ForeignKey(Profile)
	flyer = models.ForeignKey(Flyer)
	photo = models.ImageField(upload_to = 'flyerphotos',blank=True, null=True)

	def __str__(self):
		return 'photo'



class Video(models.Model):
	user = models.ForeignKey(Profile)
	flyer = models.ForeignKey(Flyer)
	video = models.FileField(upload_to = 'flyervideos' , blank=True, null=True)

	def __str__(self):
		return "video"
