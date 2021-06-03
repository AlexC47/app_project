from django.forms import ModelForm
from friends.models.friends import FriendRequest


class CategoryForm(ModelForm):
    class Meta:
        model = FriendRequest
        fields = ['sender', 'receiver', 'is_active']
        exclude = ['created_at', 'updated_at']
