from django.urls import path
from . import views

urlpatterns = [
    path('rumahku/',views.home),
    path('diriku/',views.aboutme,name='diri'),
    path('ceritakan/',views.dongeng,name='dongeng')
]