from django.shortcuts import render
from .models import Task, Tag
from django.views.generic import ListView, DetailView
# Create your views here.

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    # def get_context_data(self,**kwargs):
    #     context = super(TaskListView, self).get_context_data(**kwargs)
    #     context['task_list'] = Task.objects.all()
    #     return context

class TaskDetailView(DetailView):
    model = Task


