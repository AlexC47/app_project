from django.forms import ModelForm
from needs.models.tags import TagModel


class TagForm(ModelForm):
    class Meta:
        model = TagModel
        fields = ['name', 'special_tag']
        exclude = ['user','is_active', 'created_at', 'updated_at']
