from django.db import models
from django.conf import settings 

class Payment_type(models.Model):
    type_name = models.CharField(max_length=128)
    def __str__(self):
        return self.type_name
    


class Skill(models.Model):
    skill_name = models.CharField(max_length=128)


    def __str__(self):
        return self.skill_name
    





class Freelancer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    registration_date = models.DateField(auto_now_add=True) 
    location = models.CharField(max_length = 255 )
    profile_pic = models.ImageField(default = 'apps.png')
    overview = models.TextField()
    bid = models.DecimalField(max_digits=8,decimal_places=0, null = True)
    skill = models.ManyToManyField(Skill)
    def __str__(self):
        return self.user.username

class Portfolio(models.Model):
    freelancer = models.ForeignKey(Freelancer,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    short_description = models.TextField()
    skill = models.ManyToManyField(Skill)
    def __str__(self):
        return self.project_name

class Images(models.Model):
    image = models.ImageField()
    portfolio = models.ForeignKey(Portfolio,null = True , blank =True, on_delete=models.SET_NULL)
    def __str__(self):
        return self

class Certification  (models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete = models.CASCADE)
    certification_name = models.CharField(max_length = 255)
    provider = models.CharField(max_length = 255)
    description = models.TextField()
    date_earned = models.DateField()
    certification_link = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name
    

class Test(models.Model):
    test_name = models.CharField(max_length=128)
    test_link = models.TextField()
    def __str__(self):
        return self.test_name
    

class Test_result(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete = models.CASCADE)
    test = models.ForeignKey(Test,on_delete=models.SET_NULL,null = True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(default = None , null =True)
    test_result_link = models.TextField(default = None, null =True)
    score = models.DecimalField(max_digits = 5 , decimal_places = 2 , default = None, null =True)
    display_on_screen = models.BooleanField(default = None, null =True)
    def __str__(self):
        return self.freelancer
    
class Membership(models.Model):
    payment = models.OneToOneField(Payment_type, on_delete=models.SET_NULL , null =True)
    payment_amount = models.DecimalField(max_digits=8 , decimal_places=2,null = True)
    status = models.CharField(max_length = 255)
    renewal_date = models.DateField()
    def __str__(self):
        return self.status


# Create your models here.
