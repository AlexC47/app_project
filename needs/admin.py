from django.contrib import admin
from needs.models.categories import CategoryModel
from needs.models.tags import TagModel
from needs.models.needs import NeedModel, NeedTemplateModel
# Register your models here.


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'special_tag', 'is_active')\



@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'special_tag', 'is_active')\



@admin.register(NeedModel)
class NeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'special_tag', 'is_active')


@admin.register(NeedTemplateModel)
class NeedTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'need')