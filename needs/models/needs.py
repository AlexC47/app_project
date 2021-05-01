from django.db import models
from django.contrib.auth import get_user_model
from app_project.models import CustomModel
from utils.constants import PRIVACY_TYPES

AuthUserModel = get_user_model()


class Need(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    special_tag = models.BooleanField(default=None)
    active = models.BooleanField(default=False)


class Category(CustomModel):
    name = models.CharField(max_length=255, null=False)
    special_tag = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class Tag(CustomModel):
    name = models.CharField(max_length=255, null=False)
    special_tag = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class NeedCategory(CustomModel):
    need = models.ForeignKey(Need, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class NeedTag(CustomModel):
    need = models.ForeignKey(Need, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class UserNeed(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    need = models.ForeignKey(Need, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=PRIVACY_TYPES, null=False, default='Friends')
    scale = models.IntegerField(null=False, default=1)
    is_active = models.BooleanField(default=False)
    is_group = models.BooleanField(default=False)
    # pending_list = models.ForeignKey(AuthUserModel, )
    pending_request = models.BooleanField(default=False)
    # confirmed_with =
    ongoing = models.BooleanField(default=False)
