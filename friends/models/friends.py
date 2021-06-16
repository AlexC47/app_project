from django.db import models
from app_project.models import CustomModel
from users.models import AuthUser
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()


class FriendRequest(CustomModel):
    sender = models.ForeignKey(AuthUserModel, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(AuthUser, related_name='receiver', on_delete=models.CASCADE)
    is_active = models.BooleanField(null=False, default=True)  # blank=True
