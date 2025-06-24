from django.shortcuts import render
from . models import About
from . forms import FormBarang

def home(request):
    about = About.objects.first()
    return render(request,'index.html', {'about':about})

def aboutme(request):
    return render(request,'profil/index.html')

def dongeng(request):
    return render(request,'dongeng.html')

def form_brg(request):
    form_brg = FormBarang()
    return render(request,'tambah_brg.html',{'form_brg':form_brg})