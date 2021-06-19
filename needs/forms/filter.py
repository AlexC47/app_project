from django import forms
from needs.models import NeedTemplateModel, TagModel, CategoryModel


class SearchAndFilterNeeds(forms.Form):
    search_by = forms.CharField(max_length=255, required=False, label='Search by name')

    tags = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(),
        required=False,
        label='tags',
    )

    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(),
        required=False,
        label='category',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        tags = TagModel.objects.all()
        tag_choices = tuple([(tag.id, tag.name) for tag in tags])
        self.fields['tags'].choices = tag_choices
        categories = CategoryModel.objects.all()
        category_choices = tuple([(category.id, category.name) for category in categories])
        self.fields['categories'].choices = category_choices

    def clean_tags(self):
        tags = self.cleaned_data.get('tags', [])

        try:
            tags = [int(tag_id) for tag_id in tags]
        except ValueError:
            raise forms.ValidationError('Tag ID must be integer')

        return tags

    def clean_categories(self):
        categories = self.cleaned_data.get('categories', [])

        try:
            categories = [int(category_id) for category_id in categories]
        except ValueError:
            raise forms.ValidationError('Category ID must be integer')

        return categories

    def get_filtered_needs(self):
        if self.is_valid():
            search_term = self.cleaned_data.get('search_by', None)
            tags = self.cleaned_data.get('tags', [])
            categories = self.cleaned_data.get('categories', [])

            need_list = NeedTemplateModel.objects.order_by('-created_at')

            if search_term:
                need_list = need_list.filter(need__name__icontains=search_term)

            if tags:
                tags_set = set(tags)
                needs_ids = set()
                for need in need_list:
                    need_tag_ids = set([
                        tag_data[0]
                        for tag_data in need.tag.values_list('id')
                    ])

                    if need_tag_ids.issuperset(tags_set):
                        needs_ids.add(need.id)

                need_list = need_list.filter(id__in=needs_ids)

            if categories:
                categories_set = set(categories)
                needs_ids = set()
                for need in need_list:
                    need_category_ids = set([
                        category_data[0]
                        for category_data in need.category.values_list('id')
                    ])

                    if need_category_ids.issuperset(categories_set):
                        needs_ids.add(need.id)

                need_list = need_list.filter(id__in=needs_ids)

            return need_list

        return NeedTemplateModel.objects.all()
