from django.urls import path
from schoolManagement import views

urlpatterns = [
    path('teacher-profile', views.teacherProfile),
    path('teacher-courses', views.teacherCourse),
    path('teacher-attendance', views.teacherAttendance),
    path('teacher-announcement', views.teacherAnnouncement),
    path('edit-teacher-profile/<int:teacher_id>', views.teacherEditProfile),
    path('update-teacher-profile/<int:teacher_id>', views.teacherUpdateProfile),
    path('admin-add-course', views.adminAddCourse),
    path('edit-admin-course/<int:courseId>', views.adminEditCourse), 
    path('admin-courses/delete/<int:courseId>', views.adminDeleteCourse),
    path('update-admin-course/<int:courseId>', views.adminUpdateCourse),
    path('admin-courses', views.adminCourse),
    path('update-attendance-record', views.updateAttendanceRecord),
    path('admin-profile', views.adminProfile),
    path('edit-admin-profile/<int:admin_id>', views.adminEditProfile),
    path('update-admin-profile/<int:admin_id>', views.adminUpdateProfile),
]