from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models.user import Profile

AuthUserModel = get_user_model()


@receiver(post_save, sender=AuthUserModel)
def create_profile(instance, created, **kwargs):
    if created:
        Profile(user=instance).save()
