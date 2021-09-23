from django.http import HttpResponse
from django.shortcuts import render
from users.models import Statistics
from random import shuffle
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()


def homepage_view(request):
    statistics = Statistics.objects.order_by('-completed')
    user = request.user
    if user.is_authenticated:
        friends = list(user.profile.friends.all())
        # shuffle(friends)
        user_stats, created = Statistics.objects.get_or_create(user=user)
        commitments = user_stats.commitments
        commitment_number = commitments[0]
        helped_number = commitments[1]
        commitment_details = commitments[2]
        private_commitments = commitments[3]
        unseen_notifications = user.notifications.exclude(seen=True)
    else:
        friends = 0
        commitment_number = 0
        helped_number = 0
        commitment_details = 0
        private_commitments = 0
        unseen_notifications = 0

    return render(request, 'homepage.html', {
        'user': user,
        'friends': friends,
        'statistics': statistics[:5],
        'commitment_number': commitment_number,
        'helped_number': helped_number,
        'commitment_details': commitment_details,
        'private_commitments': private_commitments,
        'unseen_notifications': unseen_notifications,
        'brand': 'Hi, friend !',
        'motto': 'Want to help out ?',
    })


def contact_view(request):
    return render(request, 'contact.html')
