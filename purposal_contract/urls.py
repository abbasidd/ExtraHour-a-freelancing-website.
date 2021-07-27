
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^purposal/(?P<job_id>\d+)/$',
        views.purposal, name='purposal'),
        url(r'^message_listing/$',
        views.message_listing, name='message_listing'),
        url(r'^contract/(?P<purposal_id>\d+)/(?P<freelancer_id>\d+)/$',
        views.contract, name='contract'),
        url(r'^client/$',  views.client, name='client'),
        url(r'^activate/(?P<purposal_id>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
      #   url(r'^message/(?P<client_id>\d+)/(?P<freelancer_id>\d+)/(?P<purposal_id>\d+)/$',
      #   views.message, name='message'),

       # rl(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login')
    
]
