from django.urls import path, include
from needs.views.my_needs import my_needs_view
from needs.views.my_needs import MyNeedDetailsView

urlpatterns = [
    path('', my_needs_view, name='my_needs'),
    path('details/<int:id>/', MyNeedDetailsView.as_view, name='my_need_details'),

]
