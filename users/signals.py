from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from users.models import Profile, Notification
from needs.models import UserNeedModel
from friends.models import FriendRequest
from django.shortcuts import reverse

AuthUserModel = get_user_model()


@receiver(post_save, sender=AuthUserModel)
def create_profile(instance, created, **kwargs):
    if created:
        Profile(user=instance).save()


@receiver(post_save, sender=FriendRequest)
def create_friend_request_notification(instance, created, **kwargs):
    if created:
        user = instance.receiver
        notification = Notification(
            user=user,
            content_object=instance,
            message='New friend request.',
            link=reverse('friends:friends'),
        )
        notification.save()


@receiver(pre_save, sender=UserNeedModel)
def create_user_need_notification(instance, **kwargs):
    print(instance.user.pk)
    print(AuthUserModel.pk)
    if instance.pk:
        if instance.user != AuthUserModel:
            notification = Notification(
                user=instance.user,
                content_object=instance,
                message='New need interaction',
                link=reverse('needs:my_needs'),
            )
            notification.save()
