from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Examination(models.Model):
    student = models.CharField(max_length=100,null=False,blank=True)
    type = models.CharField(max_length=100,null=False,blank=True)
    marks = models.CharField(max_length=100,null=False,blank=True,default=0)
    percentage = models.DateField(max_length=30,null=False,blank=True,default=0)
    academic_year = models.CharField(max_length=100,null=False,blank=True)
    status = models.CharField(max_length=30,null=False,blank=True,default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
