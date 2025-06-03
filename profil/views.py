from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def aboutme(request):
    return render(request,'profil/index.html')

def dongeng(request):
    return render(request,'dongeng.html')