from django.urls import path, include
from users.views.notifications import NotificationRemove, NotificationSeen

app_name = 'notifications'

urlpatterns = [
    path('remove/<int:id>/', NotificationRemove.as_view(), name='notification-remove'),
    path('seen/<int:id>/', NotificationSeen.as_view(), name='notification-seen'),
]
