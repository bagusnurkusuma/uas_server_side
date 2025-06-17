from django.shortcuts import render
from . models import About

def home(request):
    about = About.objects.first()
    return render(request,'index.html', {'about':about})

def aboutme(request):
    return render(request,'profil/index.html')

def dongeng(request):
    return render(request,'dongeng.html')