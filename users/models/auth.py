from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password):
        if not first_name:
            raise ValueError('First name required.')

        if not last_name:
            raise ValueError('Last name required.')

        if not email:
            raise ValueError('Email required.')

        user = self.model(first_name=first_name, last_name=last_name, email=email, password=password)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(first_name, last_name, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class AuthUser(AbstractUser):
    username = None
    first_name = models.CharField(_('first name'), max_length=150, null=False)
    last_name = models.CharField(_('last name'), max_length=150, null=False)
    email = models.EmailField(_('email address'), null=False, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AuthUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.__str__()
