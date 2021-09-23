from django.urls import path, include
from needs.views.needs import needs_list, CategoryView, TagView, NeedView, NeedTemplateView, HelpNeedView,\
    StopHelpView, ConfirmHelpView, ResetNeedView, CompletedNeedView, OngoingNeedView
from needs.views.add_need import AddNeedToProfileView
from needs.views.my_needs import RemoveNeedView, MyNeedDetailsView

app_name = 'needs'

urlpatterns = [
    path('', needs_list),
    path('my_needs/', include('needs.urls.my_needs')),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('tags/', TagView.as_view(), name='tags'),
    path('needs/', NeedView.as_view(), name='needs'),
    path('list/', NeedTemplateView.as_view(), name='needs_templates_list'),
    path('add-user-need/<int:id>/', AddNeedToProfileView.as_view(), name='add_user_need'),
    path('remove/<int:id>/', RemoveNeedView.as_view(), name='remove'),
    path('help/<int:id>/', HelpNeedView.as_view(), name='help'),
    path('stop-help/<int:id>/', StopHelpView.as_view(), name='stop-help'),
    path('confirm/<int:id1>/<int:id2>/', ConfirmHelpView.as_view(), name='confirm'),
    path('reset/<int:id>/', ResetNeedView.as_view(), name='reset'),
    path('completed/<int:id>/', CompletedNeedView.as_view(), name='completed'),
    path('ongoing/<int:id>/', OngoingNeedView.as_view(), name='ongoing'),
    path('details/<int:id>/', MyNeedDetailsView.as_view(), name='details'),

]
