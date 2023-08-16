from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *
urlpatterns = [
    path('registration/',SignUpView.as_view(),name='Registration'),
    path('login/', LoginUser.as_view(), name='Login'),
    path('logout/',logout_view,name='Logout'),
]
