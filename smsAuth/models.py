from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False,blank=True,null=True)
    is_teacher = models.BooleanField(default=False,blank=True,null=True)
    is_parent = models.BooleanField(default=False,blank=True,null=True)
    is_payment = models.BooleanField(default=False,blank=True,null=True)
    is_exam = models.BooleanField(default=False,blank=True,null=True)
    is_admin = models.BooleanField(default=False,blank=True,null=True)
    status = models.CharField(max_length=30,null=False,blank=True,default=True)
    
