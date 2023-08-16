from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *
urlpatterns = [
    path('',index.as_view(),name='HomePage'),
    path('confirmed/',ConfirmedTask.as_view(),name='Confirm'),
    path('tasks/',MyTasks.as_view(),name='MyTasks'),
    path('messages/',Messages.as_view(),name='Messages'),
    path('requests/',MyRequests.as_view(),name='MyRequests'),
    path('members/',include('members.urls')),
    path('add_task/',CreateTask.as_view(),name="AddTask"),
    path('task/<slug:task_slug>/',TaskView.as_view(),name="TaskView"),
    path('change/<slug:task_slug>/',ChangeTask.as_view(),name="ChangeTask")
]
