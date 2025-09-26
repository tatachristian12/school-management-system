from django.urls import path
from schoolManagement import views


urlpatterns = [
    path('teacher-profile', views.teacherProfile),
    path('teacher-courses', views.teacherCourse),
    path('teacher-attendance', views.teacherAttendance),
    path('teacher-announcement', views.teacherAnnouncement),
    path('edit-teacher-profile', views.teacherEditProfile),
    path('update-teacher-profile', views.teacherUpdateProfile),
    path('teacher-add-course', views.teacherAddCourse),
    path('update-attendance-record', views.updateAttendanceRecord),
    path('admin-profile', views.adminProfile),
    path('admin-manage-student-account', views.adminManageStudentAccount),
    # path('admin-manage-student-account', views.adminManageStudentAccount),
    path('admin-staff-accounts', views.adminStaffAccounts),


]