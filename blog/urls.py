from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('post_blog/' ,  views.post_blog , name= 'post_blog'),
    path('' ,  views.blog , name= 'blog'),
     path('post_comment' ,  views.post_comment , name= 'post_comment'),
    path('blog_single/' ,  views.blog_single , name= 'blog_single'),
       url(r'^blog_single/(?P<id>\d+)/$',
        views.blog_single, name='blog_single'),
    

]