from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views.account import profile_view


urlpatterns = [
    path('', profile_view, name='profile'),

]
