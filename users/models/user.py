from django.db import models
from app_project.models import CustomModel
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()

# Create your models here.


class Profile(CustomModel):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, related_name='profile')
    about = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)
    avatar = models.ImageField(upload_to='profiles', default=None, null=True)
