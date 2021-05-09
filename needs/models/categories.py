from django.db import models
from app_project.models import CustomModel
# from .needs import NeedModel


class CategoryModel(CustomModel):
    name = models.CharField(max_length=255, null=False, unique=True)
    special_tag = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


# class NeedCategoryModel(CustomModel):
#     need = models.ForeignKey(NeedModel, on_delete=models.CASCADE)
#     category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
