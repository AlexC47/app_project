from django.forms import ModelForm
from users.models.user import Profile


class MyProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'city', 'country', 'avatar']
        exclude = ['user']