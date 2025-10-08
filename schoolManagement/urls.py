from django.urls import path
from schoolManagement import views


urlpatterns = [
    path('teacher-profile', views.teacherProfile),
    path('teacher-courses', views.teacherCourse),
    path('teacher-attendance', views.teacherAttendance),
    path('teacher-announcement', views.teacherAnnouncement),
    path('teacher-announcement/<int:ann_id>/', views.teacherAnnouncementDetail),
    path('teacher-announcement/edit/<int:ann_id>/', views.editTeacherAnnouncement),
    path('teacher-announcement/delete/<int:ann_id>/', views.deleteTeacherAnnouncement),
    path('edit-teacher-profile/<int:teacher_id>', views.teacherEditProfile),
    path('update-teacher-profile/<int:teacher_id>', views.teacherUpdateProfile),
    path('teacher-add-course', views.teacherAddCourse),
    path('update-attendance-record', views.updateAttendanceRecord),
    path('admin-profile', views.adminProfile),
    path('admin-manage-student-account', views.adminManageStudentAccount),
    # path('admin-manage-student-account', views.adminManageStudentAccount),
    path('admin-staff-accounts', views.adminStaffAccounts),
    path('edit-admin-profile/<int:admin_id>', views.adminEditProfile),
    path('update-admin-profile/<int:admin_id>', views.adminUpdateProfile),

]