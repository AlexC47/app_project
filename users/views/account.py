import django.contrib.auth
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from users.forms.myprofile import MyProfileForm, MyDetailsForm

# Create your views here.
AuthUserModel = get_user_model()


def login_view(request):
    return render(request, 'users/login.html')


def profile_view(request):
    return render(request, 'users/profile.html')


# @login_required
class MyProfileView(View):
    def get(self, request):
        profile_form = MyProfileForm(instance=request.user.profile)
        # details_form = MyDetailsForm(instance=request.user)

        return render(request, 'users/profile.html', {
            'profile_form': profile_form,
            # 'details_form': details_form,
        })

    def post(self, request):
        profile_form = MyProfileForm(request.POST, request.FILES, instance=request.user.profile)
        profile_form.save()

        # details_form = MyDetailsForm(request.Post, instance=request.user)
        # details_form.save()


        messages.success(request, 'Profile successfully updated')

        return redirect('/users/profile/')


def friends_view(request):
    return render(request, 'users/friends.html')


def logout_view(request):
    django.contrib.auth.logout(request)
    return redirect('/')
