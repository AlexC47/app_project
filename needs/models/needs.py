from django.db import models
from django.contrib.auth import get_user_model
from app_project.models import CustomModel
from utils.constants import PRIVACY_TYPES
from .pending import UserNeedPending

AuthUserModel = get_user_model()


class NeedModel(CustomModel):
    # user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    special_tag = models.BooleanField(default=None)
    is_active = models.BooleanField(default=False)


class UserNeedModel(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    need = models.ForeignKey(NeedModel, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=PRIVACY_TYPES, null=False, default='Friends')
    scale = models.IntegerField(null=False, default=1)
    is_active = models.BooleanField(default=False)
    is_group = models.BooleanField(default=False)
    pending_list = models.ForeignKey(UserNeedPending, default=None , on_delete=models.CASCADE)
    pending_request = models.BooleanField(default=False)
    # confirmed_with =
    ongoing = models.BooleanField(default=False)
