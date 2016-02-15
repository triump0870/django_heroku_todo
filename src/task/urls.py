from django.conf.urls import url
from .views import TaskListView, TaskDetailView

urlpatterns = [
    url(r'^$', TaskListView.as_view(), name='list'),
    url(r'^(?P<slug>[-\w]+)/$', TaskDetailView.as_view(), name='detail'),
]
