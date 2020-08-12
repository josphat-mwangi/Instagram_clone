from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length=60)
    image_caption=models.TextField()
    likes=models.IntegerField(default=0)
    comments=models.TextField()
    image = models.ImageField(upload_to='images/',blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile=models.ForeignKey('Profile',on_delete=models.CASCADE)



    @classmethod
    def photo_display(cls):
       photos = cls.objects.filter()
       return photos 

    def __str__(self):
        return f'{self.image_name }'


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(default='default.jpeg', upload_to='images/')
    bio = models.CharField(max_length=500)

    def save_profile(self):
        self.save()
    
    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile
    
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

    def __str__(self):
        return f'{self.user.username} Profile'
