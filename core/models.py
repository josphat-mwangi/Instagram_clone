from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length=60)
    image_caption=models.TextField()
    likes=models.IntegerField(default=0)
    comments=models.TextField()
    image = models.ImageField(upload_to='images/',blank=True)
    profile=models.ForeignKey('Profile',on_delete=models.CASCADE)


    def __str__(self):
        return Image


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_pics')
    bio = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.user.username} Profile'
