from django.db import models
from datetime import date
from django.conf import settings

class Company (models.Model):
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    def __str__(self):
        return self.company_name


class Hire_manager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    profile_pic = models.ImageField(default = 'apps.png')
    registration_date = models.DateField(default=date.today)
    location  = models.CharField(max_length=255)
    company = models.ForeignKey(Company , null =True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.user.username
# Create your models here.
