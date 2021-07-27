from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('login' ,  views.Login , name= 'login'),
    path('about_us' ,  views.about_us , name= 'about_us'),
    path('contact' ,  views.contact , name= 'contact'),
    path('blog' ,  views.blog , name= 'blog'),
    path('logout' ,  views.Logout , name= 'logout'),
    path('signup', views.signup, name ='signup'),
    path('',views.home, name= 'home'),
    path('reset_done',views.reset_done, name= 'reset_done'),
    path('check_username_exist',views.check_username_exist, name= 'check_username_exist'), 
    
    url(r'^reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.reset_confirm, name='reset_confirm'),
    path('reset_form',views.reset_form, name= 'reset_form'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

       # rl(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login')
    
]
