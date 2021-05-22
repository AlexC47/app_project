from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views.account import logout_view
from users.views.register import RegisterView

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
]
