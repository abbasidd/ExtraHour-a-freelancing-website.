from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    type = models.BooleanField( default=False )
# @receiver(post_save,sender=User)
# def created(sender,instance,**keywrd):

    