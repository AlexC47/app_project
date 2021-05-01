import django.contrib.auth
from django.shortcuts import render, redirect

# Create your views here.


def login_view(request):
    return render(request, 'users/login.html')


def profile_view(request):
    return render(request, 'users/profile.html')


def friends_view(request):
    return render(request, 'users/friends.html')


def logout_view(request):
    django.contrib.auth.logout(request)
    return redirect('/')
