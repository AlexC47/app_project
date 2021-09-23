from django.db import models
from django.contrib.auth import get_user_model
import secrets
from app_project.models import CustomModel
from django.conf import settings
from django.utils import timezone
from utils.constants import ACTIVATION_AVAILABILITY_DICT

AuthUser = get_user_model()


class Activation(CustomModel):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, default=secrets.token_hex(32))
    activated_at = models.DateTimeField(null=True, default=None)
    expires_at = models.DateTimeField(default=timezone.now() + timezone.timedelta(**ACTIVATION_AVAILABILITY_DICT))
