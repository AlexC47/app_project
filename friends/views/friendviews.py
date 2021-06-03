from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from users.models.auth import AuthUser
from friends.models import FriendRequest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages


@login_required
def send_request(request, id):
    sender = request.user
    receiver = AuthUser.objects.get(id=id)
    friend_request, created = FriendRequest.objects.get_or_create(sender=sender, receiver=receiver)

    if created:
        # return redirect(reverse('friends:friends'))
        messages.success(request, 'Friend Request Sent.')
        return redirect(reverse('friends:friends'))
        # return redirect(reverse('friends:friends'), 'Friend Request Sent')
    else:
        # return redirect(reverse('friends:friends'), 'Request Already Sent')
        # return HttpResponse('Request Already Sent')
        messages.error(request, 'Request already sent.')
        return redirect(reverse('friends:friends'))


@login_required
def accept_request(request, id):
    friend_request = FriendRequest.objects.get(id=id)
    receiver = request.user
    sender = friend_request.sender
    receiver.profile.friends.add(sender)
    sender.profile.friends.add(receiver)
    friend_request.is_active = False
    friend_request.save()

    return redirect(reverse('friends:friends'))


@login_required
def friends_view(request):
    all_users = AuthUser.objects.exclude(email=request.user)
    friend_requests = FriendRequest.objects.filter(receiver=request.user, is_active=True)

    return render(request, 'friends.html', {
        'all_users': all_users,
        'friend_requests': friend_requests,
    })
