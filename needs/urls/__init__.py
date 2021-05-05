from django.urls import path, include
from needs.views.my_needs import my_needs_view
from needs.views.needs import needs_list, CategoryView, TagView, NeedView

app_name = 'needs'

urlpatterns = [
    path('', needs_list, name='list'),
    path('my_needs/', include('needs.urls.my_needs')),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('tags/', TagView.as_view(), name='tags'),
    path('needs/', NeedView.as_view(), name='needs'),


]
