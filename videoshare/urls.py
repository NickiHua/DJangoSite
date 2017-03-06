from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.login, name='login'),
    url(r'^login/$',views.auth_login,name = 'auth_login'),
    url(r'^regist/$',views.auth_register,name = 'register'),
    #url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.auth_logout,name = 'logout'),
    url(r'^videoshare/$', views.listvideo, name = 'list_video'),
]