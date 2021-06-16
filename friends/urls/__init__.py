from django.urls import path, include
from friends.views.friendviews import send_request, friends_view, accept_request, remove_friend, friend_profile_view

app_name = 'friends'

urlpatterns = [
    path('', friends_view, name='friends'),
    path('add-friend/<int:id>/', send_request, name='add-friend'),
    path('accept/<int:id>/', accept_request, name='accept'),
    path('remove-friend/<int:id>/', remove_friend, name='remove-friend'),
    path('profile/<int:id>/', friend_profile_view, name='friend-profile')

]
