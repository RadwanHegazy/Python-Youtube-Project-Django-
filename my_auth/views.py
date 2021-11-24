from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from my_main.models import profile
from django.contrib.auth.views import auth_login

# Create your views here.

def signup (request) :
    form = SignupForm()
    if request.method == 'POST' :
        form = SignupForm(request.POST)
        if form.is_valid() :
            user = form.save()
            auth_login(request,user=user)
            profile.objects.create(user=user,email=request.POST['email'],ch_name=request.POST['channel_name']).save()
            return redirect('home')
            
    return render(request, 'signup.html',{'form':form})


