from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html

AuthUser = get_user_model()


class RegisterForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email']

    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True, help_text=password_validators_help_text_html())
    password_confirmation = forms.CharField(label='Confirm Pass', widget=forms.PasswordInput, required=True)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')

        user = AuthUser(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        validate_password(password, user)
        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password_confirmation != password:
            raise forms.ValidationError('passwords do not match')

        return password_confirmation

    def save(self, commit=True):
        password = self.cleaned_data['password']
        email = self.cleaned_data['email']
        self.instance.username = email
        self.instance.set_password(password)

        return super().save(commit)

#
# class RegisterForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100, required=True)
#     last_name = forms.CharField(label='Last Name', max_length=100, required=True)
#     email = forms.CharField(label='email', max_length=100, required=True)
#     password = forms.CharField(
#         label='password',
#         widget=forms.PasswordInput,
#         required=True,
#         help_text=password_validators_help_text_html,
#     )
#     password_confirmation = forms.CharField(label='Confirm Pass', widget=forms.PasswordInput, required=True)
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         user = AuthUser.objects.filter(email=email).first()
#         if user:
#             raise(forms.ValidationError('email is already taken'))
#
#         return email
#
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         first_name = self.cleaned_data.get('first_name')
#         last_name = self.cleaned_data.get('last_name')
#         email = self.cleaned_data.get('email')
#
#         user = AuthUser(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#         )
#
#         validate_password(password, user)
#         return password
#
#     def clean_password_confirmation(self):
#         password = self.cleaned_data.get('password')
#         password_confirmation = self.cleaned_data.get('password_confirmation')
#
#         if password_confirmation != password:
#             raise forms.ValidationError('passwords do not match')
#
#         return password_confirmation
#
#     def save(self):
#         first_name = self.cleaned_data.get('first_name')
#         last_name = self.cleaned_data.get('last_name')
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#
#         user = AuthUser.objects.create_user(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             password=password,
#         )
#
#         return user
