from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.edit_profile,name='editProfile'),
    path('profie/edit/pas/',PasswordChangeView.as_view(template_name='edit-profile.html'),name='ch_pass'),
    path('profie/edit/pas/done/',PasswordChangeDoneView.as_view(template_name='password-change-done.html'),name='password_change_done'),

    # vide videos
    path('video/view/<int:videoId>/',views.view_video,name='Vvideo'),
    
    # like videos
    path('video/like/<int:videoId>/',views.like_video,name='likeVideo'),

    # upload videos
    path('video/upload/',views.upload_videos,name='upload'),
    
    # view user
    path('user/<str:UserName>/',views.viewUser,name='VUser'),

    # subscription 
    path('user/<str:UserName>/subscribe/',views.subscribe,name='Usubs'),

    # add comment
    path('video/<int:VideoPk>/comment/',views.addComment,name='comment'),

    # search
    path('search/results/',views.search,name='search')
]