from django.urls import path, include
from django.contrib import admin
from .views import *
# from .views import CustomLoginView
from django.shortcuts import redirect


urlpatterns = [
    path('', home,name='home'),
    path('chat/', chat,name='chat'),
    path('user-profile/', userprofile,name='userprofile'),
    path('login/', login,name='login'),
] 