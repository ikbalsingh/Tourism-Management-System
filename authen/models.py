from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique = True)
    profile_pic = models.ImageField(default = 'media/mainpage4.jpg',blank=True,null=True)

    def __str__(self):
        return self.user.username