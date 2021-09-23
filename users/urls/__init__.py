from django.urls import path, include

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('notifications/', include('users.urls.notifications')),
    path('account/', include('users.urls.account')),
    path('profile/', include('users.urls.profile')),
    path('activation/<str:token>/', include('users.urls.activation')),
]
