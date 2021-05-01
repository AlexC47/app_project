from django.urls import path, include
from needs.views.my_needs import my_needs_view


urlpatterns = [
    path('', my_needs_view, name='my_needs'),

]
