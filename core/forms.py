from django import forms
from .models import Profile,Image,Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio']
class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','image_caption']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         exclude = ['image', 'image_caption',' image_name',]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','image','date_commented']