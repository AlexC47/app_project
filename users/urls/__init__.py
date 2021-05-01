from django.urls import path, include
from users.views.account import login_view, logout_view
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', include('django.contrib.auth.urls')),
    # path('', include('users.urls.account')),
    path('account/', include('users.urls.account')),
    path('profile/', include('users.urls.profile')),

]
