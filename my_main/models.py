from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.




class Video (models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_video')
    title = models.TextField(max_length=200)
    video_img = models.ImageField(upload_to='static/video-fg-images/')
    video = models.FileField(upload_to='static/users-videos/')
    caption = models.TextField(max_length=1000)
    views = models.ManyToManyField(User,related_name='videoViews', blank=True,null=True)
    likes = models.ManyToManyField(User,related_name='VideoLikes', blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str(self.title)


class profile (models.Model) :
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    ch_name = models.CharField(max_length=150)
    fg = models.ImageField(upload_to='static/fg-images/',default='static/fg-images/def/def_user.png')
    bg = models.ImageField(upload_to='static/fg-images/',default='static/fg-images/def/def_bg.jpg')
    subs = models.ManyToManyField(User,related_name='subs', blank=True,null=True)
    email = models.EmailField(max_length=100,null=True,blank=True)

    def __str__(self) :
        return str(self.user)

class Comment (models.Model) :
    user = models.ForeignKey(User,related_name='user_comment',on_delete=models.CASCADE)
    for_video = models.ForeignKey(Video,related_name='video_comt',on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__ (self) :
        return str(self.user)
    
