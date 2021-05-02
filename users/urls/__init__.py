from django.urls import path, include
from users.views.account import login_view, logout_view
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # path('', include('users.urls.accounts')),
    path('account/', include('users.urls.account')),
    path('profile/', include('users.urls.profile')),

]
