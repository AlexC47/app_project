from django.http import HttpResponse
from django.shortcuts import render
from users.models.auth import AuthUser
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()


def homepage_view(request):
    return render(request, 'homepage.html', {
        'brand': 'Hi, friend !',
        'motto': 'Want to help out ?',
    })


def contact_view(request):
    return render(request, 'contact.html')
