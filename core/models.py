from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length=60)
    image_caption=models.TextField()
    likes=models.IntegerField(default=0)
    # comments=models.TextField()
    image = models.ImageField(upload_to='images/',blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile=models.ForeignKey('Profile',on_delete=models.CASCADE)
   



    @classmethod
    def photo_display(cls):
       photos = cls.objects.filter()
       return photos 
    
    @classmethod
    def get_single_photo(cls,id):
        image = cls.objects.get(pk=id)
        return image
    
   

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

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey('Post',on_delete=models.CASCADE)
    comment = models.CharField(max_length=150, blank=True)
    date_commented = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_commented']

    def save_comment(self):
        self.save()
    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id)
        return comments

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    @classmethod
    def get_single_photo(cls,id):
        image = cls.objects.get(pk=id)
        return image