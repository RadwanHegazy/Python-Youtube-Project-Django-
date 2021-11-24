from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import models
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from my_auth.forms import UpdateProfileForm, UploadVideos
from .models import Comment, Video
# Create your views here.

def home (request) :
    videos = Video.objects.all().order_by('-date')
    return render(request, 'home.html',{'videos':videos})

def profile (request) :
    getvideos = Video.objects.filter(user=request.user)
    get_prof = models.profile.objects.get(user=request.user)
    return render(request,'profile.html',{'get':get_prof,'videos':getvideos})

def upload_videos (request) :
    if request.method == 'POST' :
        title = request.POST['title']
        caption = request.POST['caption']
        video_image = request.FILES.get('video_img')
        video = request.FILES.get('video')
        Video.objects.create(user=request.user,title=title,caption=caption,video=video,video_img=video_image).save()
        return redirect('home')
    return render(request,'upload-videos.html')


def edit_profile (request) :
    userId = request.user.id
    getuser = User.objects.get(id=userId)
    data = models.profile.objects.get(user=getuser)
    if request.method == 'POST' : 
        form = UpdateProfileForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request,'edit-profile.html')


def view_video (request, videoId) :
    if request.user.is_authenticated == False :
        return redirect('login')
    video = Video.objects.get(id=videoId)
    videos = Video.objects.all().order_by('?').exclude(id=videoId)
    if request.user in video.views.all() :
        pass
    else :
        video.views.add(request.user)
    comments = Comment.objects.filter(for_video=video).order_by('-date')
    return render(request,'view-video.html',{'video':video,'videos':videos,'comments':comments})


def like_video (request, videoId) : 
    user = request.user
    video = Video.objects.get(id=videoId)
    user_is_logedin = request.user.is_authenticated
    print(user_is_logedin)
    if user in video.likes.all() :
        video.likes.remove(user)
    else :
        video.likes.add(user)
    data = {'likes':video.likes.count()}
    return HttpResponse(data['likes'])

def viewUser (request, UserName) :
    getUser = get_object_or_404(User,username=UserName)
    if request.user.username == UserName :
        return redirect('profile')
    else :
        user_videos = Video.objects.filter(user=getUser).order_by('-date')
        return render(request, 'view-user.html',{'get':getUser,'videos':user_videos})

def subscribe (request, UserName) :
    user = request.user
    getUser = get_object_or_404(User,username=UserName)
    getProfile = models.profile.objects.get(user=getUser)
    if user in getProfile.subs.all() :
        getProfile.subs.remove(user)
    else:
        getProfile.subs.add(user)
    return redirect('VUser',UserName)

def addComment (request, VideoPk) :
    user = request.user
    video = get_object_or_404(Video,pk=VideoPk)
    Comment.objects.create(for_video=video,user=user,comment=request.POST['comment'])
    return redirect('Vvideo',VideoPk)

def search (request) :
    if request.method == "POST" :
        word = request.POST['q']
        data = Video.objects.filter(caption__icontains=word,title__icontains=word).order_by('-date')
        return render(request,'search.html',{'videos':data})
        

    return render(request,'search.html')