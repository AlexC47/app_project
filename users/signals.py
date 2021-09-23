from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth import get_user_model, get_user
from users.models import Profile, Notification, Activation
from needs.models import UserNeedModel
from friends.models import FriendRequest
from django.shortcuts import reverse
from users.emails import send_activation_email

AuthUserModel = get_user_model()


@receiver(post_save, sender=AuthUserModel)
def create_profile(instance, created, **kwargs):
    if created:
        Profile(user=instance).save()


@receiver(pre_save, sender=AuthUserModel)
def inactivate_user(instance, **kwargs):
    if not instance.pk:
        instance.is_active = False
        instance.password = None


@receiver(post_save, sender=AuthUserModel)
def set_activation_details(instance, created, **kwargs):
    if created:
        activation = Activation(user=instance)
        activation.save()

        send_activation_email(activation)


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


@receiver(m2m_changed, sender=UserNeedModel.pending_list.through)
def create_user_need_notification(instance, action, **kwargs):
    if action == 'post_add':
        print('m2m signal instance_user:', instance.user)
        print('m2m signal logged_in_user:', 0)
        if instance.user != 0:
            notification = Notification(
                user=instance.user,
                content_object=instance,
                message='New need interaction',
                link=reverse('needs:details', args=(instance.id,)),
                # link=reverse('needs:my_needs'),
            )
            notification.save()
