import django.contrib.auth
from django.shortcuts import render, redirect
from django.views import View
from users.models.user import Profile
from django.contrib.auth import get_user_model
from users.forms.myprofile import MyProfileForm

# Create your views here.
AuthUserModel = get_user_model()


def login_view(request):
    return render(request, 'users/login.html')


def profile_view(request):
    return render(request, 'users/profile.html')


class MyProfileView(View):
    def get(self, request):
        # profile = Profile.objects.get(id=AuthUserModel)
        # profile = request.user.Profile()
        # profile = request.user.get_profile()
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


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {
            'form': form
        }

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_register_email(user)
            return redirect(reverse('users:account:login'))
