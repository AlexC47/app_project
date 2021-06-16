from django.forms import ModelForm
from needs.models.needs import UserNeedModel


class UserNeedForm(ModelForm):
    class Meta:
        model = UserNeedModel
        fields = ['name', 'special_tag']
        exclude = ['is_active', 'created_at', 'updated_at']
