from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'', views.boothlist, name='boothlist'),
    url(r'^booth/(?P<pk>\d+)/$',views.boothinfo,name='boothinfo'),
    url(r'^boothnew/',views.boothnew,name='name_new'),
    url(r'^imgnew/',views.imgnew,name='img_new'),
    url(r'^join/',views.joinsection,name='join_new'),
    url(r'^accounts/login/',views.loginsec,name='login_sec'),
    url(r'^logout/', auth_views.logout_then_login)
]