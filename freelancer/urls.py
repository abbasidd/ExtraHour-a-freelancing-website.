
from django.urls import path
from . import views

urlpatterns = [
   path('signup/', views.signup_freelancer, name='signup_freelancer'),
   path('test/', views.test, name='test'),
   path('portfolio/', views.portfolio_save, name='portfolio_save'),

       # rl(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login')
    
]
