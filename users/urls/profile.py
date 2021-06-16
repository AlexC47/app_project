from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views.account import profile_view
from users.views.account import MyProfileView


urlpatterns = [
    path('', MyProfileView.as_view(), name='profile'),
    # path('', profile_view, name='profile'),

]
