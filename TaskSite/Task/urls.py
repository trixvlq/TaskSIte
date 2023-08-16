from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *
urlpatterns = [
    path('',index.as_view(),name='HomePage'),
    path('members/',include('members.urls')),
    path('add_task/',CreateTask.as_view(),name="AddTask"),
    path('task/<slug:task_slug>/',TaskView.as_view(),name="TaskView")
]
