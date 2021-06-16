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
        notifications = request.user.notifications.filter(seen=False).all()
        seen_notifications = request.user.notifications.filter(seen=True).all()

        return render(request, 'users/profile.html', {
            'profile_form': profile_form,
            'notifications': notifications,
            'seen_notifications': seen_notifications,
        })

    def post(self, request):
        profile_form = MyProfileForm(request.POST, request.FILES, instance=request.user.profile)
        profile_form.save()

        messages.success(request, 'Profile successfully updated')

        return redirect('/users/profile/')


def friends_view(request):
    return render(request, 'users/friends.html')


def logout_view(request):
    django.contrib.auth.logout(request)
    return redirect('/')
