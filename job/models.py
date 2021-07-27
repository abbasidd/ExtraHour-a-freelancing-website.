from django.db import models
from client import models as client_model
from freelancer import models as f_model

class Expected_duration(models.Model):
    other_skill = models.ManyToManyField(f_model.Skill )
    duration_text = models.CharField(max_length=255)
    def __str__(self):
        return self.duration_text
    


class Complexity(models.Model):
    complexity_text = models.CharField(max_length=255)
    def __str__(self):
        return self.complexity_text

class Job(models.Model):
    hire_manager = models.ForeignKey(client_model.Hire_manager, on_delete=models.CASCADE)
    expected_duration = models.ForeignKey(Expected_duration , on_delete=models.SET_NULL,null = True)
    complexity = models.ForeignKey(Complexity , on_delete=models.SET_NULL,null = True)
    main_skill = models.ForeignKey(f_model.Skill,on_delete = models.CASCADE )
    payment_type = models.ForeignKey(f_model.Payment_type , on_delete=models.SET_NULL, null =True)
    description = models.TextField()
    published = models.DateTimeField(auto_now_add = True)
    payment_amount = models.IntegerField()
    title=models.TextField()
   
    def __str__(self):
        return self.title
    

# class Other_skills (models.Model):
#     job = models.ForeignKey(Job  , on_delete=models.CASCADE)
#     skill = models.ForeignKey(f_model.Skill , on_delete= models.CASCADE)

# # Create your models here.
