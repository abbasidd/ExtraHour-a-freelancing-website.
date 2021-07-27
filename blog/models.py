from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Catagory(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Catagory_detail", kwargs={"pk": self.pk})


class Tag(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return self.title

class Post(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    published = models.BooleanField(default = False)
    created_at =  models.DateTimeField( auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now_add=False , null =True,blank= True)
    published_at =  models.DateTimeField( auto_now_add=False, null =True,blank= True)
    content = models.TextField()
    pic = models.ImageField(default = 'apps.png')
    catagory = models.ManyToManyField(Catagory)
    tag = models.ManyToManyField(Tag)
    

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    title = models.CharField( max_length=255)
    published = models.BooleanField(default = False)
    created_at =  models.DateTimeField( auto_now_add=True)
    published_at =  models.DateTimeField( auto_now_add=False , null =True,blank= True)
    content = models.TextField()


    def __str__(self):
        return self.title

class Comment_reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    title = models.CharField( max_length=255)
    published = models.BooleanField(default = False)
    created_at =  models.DateTimeField( auto_now_add=True)
    published_at =  models.DateTimeField( auto_now_add=False)
    content = models.TextField()

    def __str__(self):
        return self.title