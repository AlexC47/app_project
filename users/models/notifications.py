from django.db import models
from app_project.models import CustomModel
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

AuthUserModel = get_user_model()


class Notification(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, related_name='notifications')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    message = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    seen = models.BooleanField(default=False)
