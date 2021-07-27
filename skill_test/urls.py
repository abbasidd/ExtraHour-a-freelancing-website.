
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
         url(r'^(?P<quiz_id>\d+)/$',
        views.quiz_taker, name='quiz_taker'),
        path('quizes/', views.quizes ,name='quizes'),

        path('user_ans', views.user_ans ,name='user_ans'),
        url(r'^result/(?P<quiz_taker_id>\d+)/$',
        views.result, name='result'),


       # rl(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login')
    
]
