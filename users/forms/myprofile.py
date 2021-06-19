from django.forms import ModelForm
from users.models import Profile
from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth import get_user_model


AuthUserModel = get_user_model()


class MyProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'city', 'country', 'avatar']
        exclude = ['user']

    def clean_avatar(self):
        image = self.cleaned_data.get('avatar')
        # print(get_image_dimensions(image))
        # print(image.content_type)
        # print(image.size)
        if image:
            w, h = get_image_dimensions(image)
            if image.content_type not in ['image/png', 'image/jpg', 'image/jpeg', 'image/gif', 'image/webp']:
                raise forms.ValidationError(u'Format not allowed')
            if w > 8000 or h > 8000:
                raise forms.ValidationError(u'Max width/height is 8000px')
            if image.size > 5000000:
                raise forms.ValidationError(u'File size cannot exceed 5Mb')

        return image


class MyDetailsForm(MyProfileForm):
    class Meta:
        model = AuthUserModel
        fields = ['first_name', 'last_name']
        exclude = ['user', 'email']
