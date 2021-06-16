from django.db import models
from app_project.models import CustomModel
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()

# Create your models here.


class Profile(CustomModel):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, related_name='profile')
    about = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, default='Cluj-Napoca')
    country = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='profiles', blank=False, default='default_avatar.png', null=True)
    friends = models.ManyToManyField(AuthUserModel, blank=True, related_name='friends')


class Statistics(CustomModel):
    user = models.OneToOneField(
        AuthUserModel,
        default='user_deleted',
        on_delete=models.SET_DEFAULT,
        related_name='statistics'
    )
    completed = models.PositiveIntegerField(default=0, null=False, blank=False)
    words = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='Words of Affirmation')
    touch = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='Physical Touch')
    acts = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='Acts of Service')
    gifts = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='Receiving Gifts')
    quality_time = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='Quality Time')

    @property
    def most_used_need(self):
        categories = (self.words, self.touch, self.acts, self.gifts, self.quality_time)
        most_uses_list = list(categories)
        most_uses = max(categories)
        while most_uses in most_uses_list:
            most_uses_list.remove(most_uses)

        second_best = max(most_uses_list) if len(most_uses_list) > 0 else 0
        second_best += 1 if second_best == 0 else 0
        names = [name.verbose_name for name in Statistics._meta.get_fields()[5:10]]
        fields = list(zip(names, categories))
        most_used = [name for name, field in fields if field >= second_best]

        return most_used

    @property
    def commitments(self):
        friends = self.user.profile.friends.all()
        commitments = []
        helped_list = []
        privacy = []
        private_commitments = 0
        for friend in friends:
            for need in friend.needs.all():
                if self.user in need.pending_list.all() or self.user in need.confirmed_with.all():
                    helped_list.append(friend.first_name)
                    commitments.append(need.need.need.name)
                    privacy.append(need.is_special)
                    if need.is_special:
                        private_commitments += 1

        details = zip(commitments, helped_list, privacy)
        helped = len(set(helped_list))
        commitments = len(commitments)

        return commitments, helped, details, private_commitments
