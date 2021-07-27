
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
   path('post_job/', views.post_job, name='post_job'),
   url(r'^job_single/(?P<job_id>\d+)/$',
        views.job_single, name='job_single'),
   path('job_search/', views.job_search, name='job_search'),
     path('job_listing/', views.job_listing, name='job_listing'),
       # rl(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login')
    
]
