from django.contrib import admin
from .models import Management,Announcement,Attendance
# Register your models here.
admin.site.register(Management)
admin.site.register(Announcement)
admin.site.register(Attendance)