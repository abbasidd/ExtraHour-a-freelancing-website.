"""ExtraHour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from accounts.views import home
urlpatterns = [
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    #path('api/', include(('api.urls', 'accounts'), namespace='api')),
    path('freelancer/', include(('freelancer.urls',
                                 'freelancer'), namespace='freelancer')),
    path('client/', include(('client.urls', 'client'), namespace='client')),
    path('job/', include(('job.urls', 'job'), namespace='job')),
    path('purposal_contract/', include(('purposal_contract.urls',
                                        'purposal_contract'), namespace='purposal_contract')),
    path('skill_test/', include(('skill_test.urls', 'skill_test'), namespace='skill_test')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('admin/', admin.site.urls),
    path('',home, name= 'home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
