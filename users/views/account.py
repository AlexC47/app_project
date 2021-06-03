import django.contrib.auth
from django.shortcuts import render, redirect, reverse
from django.views import View
from users.models.user import Profile
from django.contrib.auth import get_user_model
from users.forms.myprofile import MyProfileForm
from users.forms.register import RegisterForm

# Create your views here.
AuthUserModel = get_user_model()


def login_view(request):
    return render(request, 'users/login.html')


def profile_view(request):
    return render(request, 'users/profile.html')


class MyProfileView(View):
    def get(self, request):
        profile_form = MyProfileForm(instance=request.user.profile)

        return render(request, 'users/profile.html', {
            'profile': profile_form,
        })

    def post(self, request):
        form = MyProfileForm(request.POST)
        form.save()

        return redirect('/users/profile/')


def friends_view(request):
    return render(request, 'users/friends.html')


def logout_view(request):
    django.contrib.auth.logout(request)
    return redirect('/')
