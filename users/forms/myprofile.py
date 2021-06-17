from django.forms import ModelForm
from users.models import Profile
from users.models import AuthUser
from PIL import Image
from django import forms
from django.core.files.images import get_image_dimensions


class MyProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'city', 'country', 'avatar']
        exclude = ['user']

    def clean_image(self):
        image = self.cleaned_data.get['image']
        print(get_image_dimensions(image))
        if image:
            w, h = get_image_dimensions(image)
            if image.content_type not in ['png', 'jpg', 'gif']:
                raise forms.ValidationError(u'Only *.gif, *.jpg and *.png images are allowed.')
            if w > 5000 or h > 5000:
                raise forms.ValidationError(
                    u'That image is too big. The image needs to be ' + str(5000) + 'px * ' + str(
                        5000) + 'px (or less).')

        return image


class MyDetailsForm(MyProfileForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name']
        exclude = ['user', 'email']

