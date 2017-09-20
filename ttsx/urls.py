from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^[\w\d]{0,10}/?$', views.index, name='index'),
    url(r'^user/login/$', views.login, name='login'),
    url(r'^user/register/$', views.register, name='register'),
    url(r'^user/login_check/$', views.login_check, name='login_check'),
    url(r'^user/logout/$', views.logout, name='logout'),
]