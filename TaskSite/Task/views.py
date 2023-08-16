from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.utils.text import slugify
from django.db.models import Q
from .forms import TaskForm
from .models import *
class index(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = "tasks"
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(Q(receiver=user.id) | Q(author=user.id)).order_by('date')
        return queryset
# def index(request):
#     user = request.user
#
#     context = {
#         'tasks':tasks
#     }
#     return render(request,"index.html",context=context)
class ChangeTask(UpdateView):
    model = Task
    template_name = "update_task.html"
    form_class = TaskForm
    slug_url_kwarg = "task_slug"
class CreateTask(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'add_page.html'
    def form_valid(self,form):
        form.instance.author = self.request.user
        form.instance.status = Status.objects.get(id=1)
        print(form.instance)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('HomePage')
class TaskView(DetailView):
    model = Task
    template_name = "detail_task.html"
    context_object_name = "task"
    slug_url_kwarg = "task_slug"