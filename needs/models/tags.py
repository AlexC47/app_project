from app_project.models import CustomModel
from django.db import models
from .needs import NeedModel


class TagModel(CustomModel):
    name = models.CharField(max_length=255, null=False)
    special_tag = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class NeedTagModel(CustomModel):
    need = models.ForeignKey(NeedModel, on_delete=models.CASCADE)
    tag = models.ForeignKey(TagModel, on_delete=models.CASCADE)
