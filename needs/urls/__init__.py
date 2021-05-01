from django.urls import path, include
from needs.views.my_needs import my_needs_view
from needs.views.needs import needs_list

app_name = 'needs'

urlpatterns = [
    path('', needs_list, name='list'),
    path('my_needs/', include('needs.urls.my_needs')),

]
