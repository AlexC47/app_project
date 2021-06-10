from django.db import models
from django.contrib.auth import get_user_model
from app_project.models import CustomModel
from utils.constants import PRIVACY_TYPES
from .pending import UserNeedPending
from .tags import TagModel
from .categories import CategoryModel

AuthUserModel = get_user_model()


class NeedModel(CustomModel):
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
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, related_name='needs')
    need = models.ForeignKey(NeedTemplateModel, on_delete=models.CASCADE, default=None, null=False)
    type = models.CharField(max_length=255, choices=PRIVACY_TYPES, null=False, default='Friends')
    is_active = models.BooleanField(default=False)
    is_group = models.BooleanField(default=False)
    pending_list = models.ManyToManyField(AuthUserModel, blank=True, related_name='friends_pending')
    completed = models.BooleanField(default=False)
    confirmed_with = models.ManyToManyField(AuthUserModel, blank=True, related_name='friends_confirmed')
    ongoing = models.BooleanField(default=False)

    @property
    def scale_check(self):
        scale = 1
        scale += 1 if self.pending_list.count() > 0 or self.confirmed_with.count() > 0 else 0
        scale += 1 if self.confirmed_with.count() > 0 else 0
        scale += 1 if self.ongoing else 0
        scale += 1 if self.completed else 0
        return scale
