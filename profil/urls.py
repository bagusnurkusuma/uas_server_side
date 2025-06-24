from django.urls import path
from . import views

urlpatterns = [
    path('rumahku/',views.home,name='home'),
    path('diriku/',views.aboutme,name='diri'),
    path('ceritakan/',views.dongeng,name='dongeng'),
    path('tbh_brg/',views.form_brg)
]