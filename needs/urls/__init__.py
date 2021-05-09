from django.urls import path, include
from needs.views.needs import needs_list, CategoryView, TagView, NeedView, NeedTemplateView

app_name = 'needs'

urlpatterns = [
    path('', needs_list),
    path('my_needs/', include('needs.urls.my_needs')),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('tags/', TagView.as_view(), name='tags'),
    path('needs/', NeedView.as_view(), name='needs'),
    path('list/', NeedTemplateView.as_view(), name='needs_templates_list'),

]
