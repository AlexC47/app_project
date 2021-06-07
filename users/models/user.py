from django.db import models
from app_project.models import CustomModel
from django.contrib.auth import get_user_model
import os
from PIL import Image

AuthUserModel = get_user_model()

# Create your models here.


class Profile(CustomModel):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, related_name='profile')
    about = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='profiles', blank=True, default=None, null=True)
    friends = models.ManyToManyField(AuthUserModel, blank=True, related_name='friends')
