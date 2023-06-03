from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    context = {
        "group" : Group.objects.all(),
        # "teacher" : Teacher.all(),
    }
    return render(request, 'home/index.html',context)

def chat(request):
    context = {
        
    }
    return render(request, 'home/chat.html',context)

def userprofile(request):
    context = {
        
    }
    return render(request, 'home/user-profile.html',context)

def main(request):
    context = {
        "teacher" : Teacher.objects.all(),
    }
    return render(request, 'main.html',context)