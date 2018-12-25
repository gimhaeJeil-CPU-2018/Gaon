from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.boothlist,name='boothlist'),
    path('booth/<pk>',views.boothinfo,name='boothinfo'),
    path('boothnew/',views.boothnew,name='name_new'),
    path('imgnew/',views.imgnew,name='img_new'),
    path('bnew/',views.bnamenew,name='bname_new'),
    path('join/',views.joinsection,name='join_new'),
    path('accounts/login/',views.loginsec,name='login_sec'),
    path('logout/', auth_views.logout_then_login)
]