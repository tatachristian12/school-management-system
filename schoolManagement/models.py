from django.db import models
from smsAuth.models import *
from student.models import *

# Create your models here.
class Management(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_management")
    address = models.CharField(max_length=100,null=False,blank=True)
    employee_number = models.CharField(max_length=100,null=False,blank=True)
    marital_status = models.CharField(max_length=100,null=False,blank=True)
    DOB = models.CharField(max_length=30,null=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_attendance")
    Attendance_record = models.CharField(max_length=30,null=False,blank=True,default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Announcement(models.Model):
    user = models.ForeignKey(Management, on_delete=models.CASCADE, related_name="user_announcement")
    title = models.CharField(max_length=200, null=False, blank=True)
    announcement = models.CharField(max_length=500, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)