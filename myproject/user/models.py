from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
# Create your models here.

class User(AbstractUser):
    userName = models.CharField(max_length=200,blank=True,null= True)
    is_teacher = models.BooleanField(default = False)
    is_student = models.BooleanField(default = False)
    
    
    def __str__(self) -> str:
        return self.userName
    
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    body = models.TextField(max_length=500,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title