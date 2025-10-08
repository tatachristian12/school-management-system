from django.db import models
from smsAuth.models import *
from student.models import *

# Create your models here.
class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="parent_user")
    parent_of = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="user_parent")
    address = models.CharField(max_length=100,null=False,blank=True)
    status = models.CharField(max_length=30,null=False,blank=True,default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
                return f"{self.student.user.first_name} {self.student.user.last_name}"