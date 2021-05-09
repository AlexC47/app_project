from django.db import models
from django.contrib.auth import get_user_model
from app_project.models import CustomModel
from utils.constants import PRIVACY_TYPES
from .pending import UserNeedPending
from .tags import TagModel
from .categories import CategoryModel

AuthUserModel = get_user_model()


class NeedModel(CustomModel):
    # user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, unique=True)
    special_tag = models.BooleanField(default=None)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class NeedTemplateModel(CustomModel):
    need = models.ForeignKey(NeedModel, on_delete=models.CASCADE)
    tag = models.ManyToManyField(TagModel)
    category = models.ManyToManyField(CategoryModel)


class UserNeedModel(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    need = models.ManyToManyField(NeedTemplateModel)
    type = models.CharField(max_length=255, choices=PRIVACY_TYPES, null=False, default='Friends')
    scale = models.IntegerField(null=False, default=1)
    is_active = models.BooleanField(default=False)
    is_group = models.BooleanField(default=False)
    pending_list = models.ForeignKey(UserNeedPending, default=None , on_delete=models.CASCADE)
    pending_request = models.BooleanField(default=False)
    # confirmed_with =
    ongoing = models.BooleanField(default=False)
