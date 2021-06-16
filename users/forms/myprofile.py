from django.forms import ModelForm
from users.models import Profile
from users.models import AuthUser


class MyProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'city', 'country', 'avatar']
        exclude = ['user']


class MyDetailsForm(MyProfileForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name']
        exclude = ['user', 'email']

