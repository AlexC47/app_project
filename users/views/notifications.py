from django.views import View
from users.forms.register import RegisterForm
from django.shortcuts import render, redirect, reverse
from users.models import Notification


class NotificationRemove(View):
    def get(self, request, id):
        notification = Notification.objects.get(id=id)
        notification.delete()

        return redirect(reverse('users:profile'))


class NotificationSeen(View):
    def get(self, request, id):
        notification = Notification.objects.get(id=id)
        notification.seen = True
        notification.save()

        return redirect(reverse('users:profile'))
