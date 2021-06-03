from django.db import models
from app_project.models import CustomModel
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

AuthUserModel = get_user_model()


# class UserRequest(AbstractUser):
#     friends = models.ManyToManyField('UserRequest', blank=True)
#
#
# class Friendships(CustomModel):
#     sent_from = models.ForeignKey(AuthUserModel, related_name='sender', on_delete=models.CASCADE)
#     sent_to = models.ForeignKey(UserRequest, related_name='receiver', on_delete=models.CASCADE)
#     confirmed = models.BooleanField(default=False)


class FriendsList(CustomModel):
    friends = models.ManyToManyField(AuthUserModel, blank=True, related_name='friends')
    user = models.OneToOneField(AuthUserModel, related_name='owner', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.email

    def add_friend(self):
        if not account in self.friends.all():
            self.friends.add(account)

    def remove_friend(self,account):
        if account in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, removee):
        remover_friends_list = self
        remover_friends_list.remove_friend(removee)
        friends_list = FriendsList.objects.get(user=removee)
        friends_list.remove_friends(self.user)

    def is_mutual_friend(self, friend):
        if friend in self.friends.all():
            return True
        return False


class FriendRequest(CustomModel):
    sender = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, related_name='receiver')
    is_active = models.BooleanField(blank=True, null=False, default=True)

    def __str__(self):
        return self.sender.username

    def accept(self):
        receiver_friend_list = FriendsList.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = FriendsList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False
                self.save()

    def decline(self):
        self.is_active = False
        self.save()

