from django.forms import ModelForm
from needs.models.needs import NeedModel


class NeedForm(ModelForm):
    class Meta:
        model = NeedModel
        fields = ['name', 'special_tag']
        exclude = ['is_active', 'created_at', 'updated_at']
