from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
 path('signup_company/', views.signup_company , name = "signup_company"),
  path('signup_client/', views.signup_client , name = "signup_client"),
  url(r'^purposal_list/(?P<job_id>\d+)/$',
        views.purposal_list, name='purposal_list'),
  url(r'^purposal_single/(?P<purposal_id>\d+)/$',
        views.purposal_single, name='purposal_single'),
  url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
