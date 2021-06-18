from django.forms import ModelForm
from needs.models.needs import NeedTemplateModel


class NeedTemplateForm(ModelForm):
    class Meta:
        model = NeedTemplateModel
        fields = [
            'need',
            'tag',
            'category',
        ]

        labels = {
            'need': 'Description',
            'tag': 'Tag(s)',

        }