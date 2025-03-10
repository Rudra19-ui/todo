from django.views.generic import ListView, CreateView
from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    template_name = 'todo/list.html'
    model = Task

class TaskCreateView(CreateView):
    template_name = 'todo/create.html'
    model = Task
    form_class = TaskForm
    success_url = '/todo/'