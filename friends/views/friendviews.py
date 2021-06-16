from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from users.models import AuthUser
from friends.models import FriendRequest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from needs.models.needs import UserNeedModel


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
        friend_request.is_active = True
        friend_request.save()
        messages.error(request, 'Request already sent.')
        return redirect(reverse('friends:friends'))\



@login_required
def accept_request(request, id):
    friend_request = FriendRequest.objects.get(id=id)
    receiver = request.user
    sender = friend_request.sender
    receiver.profile.friends.add(sender)
    sender.profile.friends.add(receiver)
    friend_request.is_active = False
    friend_request.delete()

    return redirect(reverse('friends:friends'))\



@login_required
def remove_friend(request, id):
    removed_friend = AuthUser.objects.get(id=id)
    remover = request.user
    removed_friend.profile.friends.remove(remover)
    remover.profile.friends.remove(removed_friend)

    return redirect(reverse('friends:friends'))


@login_required
def friends_view(request):
    all_users = AuthUser.objects.exclude(email=request.user)
    friend_requests = FriendRequest.objects.filter(receiver=request.user, is_active=True)

    return render(request, 'friends.html', {
        'all_users': all_users,
        'friend_requests': friend_requests,
    })


@login_required
def friend_profile_view(request, id):
    user = AuthUser.objects.get(id=id)
    needs = UserNeedModel.objects.filter(user=id)

    return render(request, 'friend_profile.html', {
        'needs': needs,
        'user': user,
    })
