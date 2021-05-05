from django.forms import ModelForm
from needs.models.categories import CategoryModel


class CategoryForm(ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['name', 'special_tag']
        exclude = ['is_active', 'created_at', 'updated_at']