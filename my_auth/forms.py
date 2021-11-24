from my_main import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import fields

class SignupForm (UserCreationForm) :
    channel_name = forms.CharField()
    
    class meta :
        fields = ['username','email','channel_name','password1','password2']

class UpdateProfileForm (forms.ModelForm) :
    class Meta:
        model = models.profile
        fields = ['bg','fg','email','ch_name']

class UploadVideos (forms.ModelForm) :
    class Meta :
        model = models.Video
        fields = ['title','video_img','video','caption']