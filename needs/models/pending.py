from app_project.models import CustomModel
from django.db import models
# from .needs import UserNeed
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()


class UserNeedPending(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    # user_need = models.ForeignKey(UserNeed, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
