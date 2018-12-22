from django.urls import path
from . import views

urlpatterns = [
    path('',views.boothlist,name='boothlist'),
    path('booth/<pk>',views.boothinfo,name='boothinfo'),
    path('boothnew/',views.BoothNew,name='name_new')
]