from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.utils.text import slugify
from django.db.models import Q
from .forms import TaskForm
from .models import *
class index(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = "tasks"
    paginate_by = 3
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    def get_queryset(self):
        status = Status.objects.get(slug="in-progress")
        user = self.request.user
        queryset = Task.objects.filter((Q(receiver=user.id) | Q(author=user.id)) & Q(status=status)).order_by('date')
        return queryset
class DeleteTask(DeleteView):
    model = Task
    template_name = "delete.html"
    success_url = "HomePage"
class Messages(ListView):
    model = Message
    template_name = 'messages.html'
    context_object_name = "messages"
    paginate_by = 3
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Сообщения'
        return context
    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter((Q(receiver=user.id) | Q(author=user.id))).order_by('date')
        return queryset
class ConfirmedTask(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = "tasks"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        status = Status.objects.get(slug="zavershil")
        user = self.request.user
        queryset = Task.objects.filter(Q(receiver=user.id) | Q(author=user.id) & Q(status=status)).order_by('date')
        return queryset
class MyTasks(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = "tasks"
    paginate_by = 3
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(receiver=user.id).order_by('date')
        return queryset
class MyRequests(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = "tasks"
    paginate_by = 3
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(author=user.id).order_by('date')
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