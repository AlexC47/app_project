from django import forms
from django.contrib.auth import get_user_model

AuthUser = get_user_model()


class RegisterForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        email = self.cleaned_data['email']
        self.instance.username = email

        return super().save(commit)
