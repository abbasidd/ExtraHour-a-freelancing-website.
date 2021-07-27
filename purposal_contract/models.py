from django.db import models
from django.contrib.auth.models import User
from freelancer import models as f_model
from client import models as c_model
from job import models as j_model




class Purposal_status_catalog(models.Model):
    status_name = models.CharField(max_length =128)
    def __str__(self):
        return self.status_name
    

class Purposal(models.Model):
    job = models.ForeignKey(j_model.Job , on_delete=models.CASCADE)
    freelancer = models.ForeignKey(f_model.Freelancer, on_delete=models.CASCADE)
    purposal_time = models.DateTimeField(auto_now_add=True)
    payment_type = models.ForeignKey(f_model.Payment_type,on_delete=models.SET_NULL, null=True)
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    days = models.IntegerField( null=True)
    title = models.CharField(max_length = 255, null= True)
    purposal_status_catalog = models.ForeignKey(Purposal_status_catalog, on_delete=models.CASCADE)
    client_grade = models.DecimalField(max_digits=1, decimal_places=1,null=True)
    client_comment = models.TextField(null=True)
    freelancer_grade = models.DecimalField(max_digits=1, decimal_places=1,null=True)
    freelancer_comment = models.TextField(null=True)
    def __str__(self):
        return self.purposal_status_catalog.status_name

    
class Contract(models.Model):
     purposal = models.ForeignKey(Purposal,on_delete=models.CASCADE)
     company = models.ForeignKey(c_model.Company , on_delete=models.CASCADE)
     freelancer = models.ForeignKey(f_model.Freelancer , on_delete=models.CASCADE)
     start_time = models.DateTimeField(auto_now_add=True)
     end_time = models.DateTimeField(default = None , null =True)
     payment_type = models.ForeignKey(f_model.Payment_type,on_delete=models.CASCADE)
     payment_amount = models.DecimalField(max_digits=8, decimal_places=2)
     def __str__(self):
        return self.purposal

class Message_list(models.Model):
    freelancer = models.ForeignKey(f_model.Freelancer,on_delete=models.CASCADE)
    hire_manager = models.ForeignKey(c_model.Hire_manager,on_delete=models.CASCADE)

class Message(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    message_time = models.DateTimeField(auto_now_add=True )
    message_text = models.TextField(null=True)
    # parent_message = models.ForeignKey(this , on_delete=models.SET_NULL,null = True)
    purposal_status_catalog = models.ForeignKey(Purposal_status_catalog, on_delete=models.SET_NULL, null = True)
    purposal = models.ForeignKey(Purposal,on_delete=models.CASCADE)


class Recipient(models.Model):
    user = models.ForeignKey(User,  on_delete=models.SET_NULL, null = True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    is_read =models.BooleanField()


class Attachment(models.Model):
    attachment_link = models.FileField(upload_to='messages/')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
# Create your models here.
