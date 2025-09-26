from django.urls import path # type: ignore
from student import views


urlpatterns = [
    path('student-profile', views.studentProfile),
    path('student-courses', views.studentCourse),
    path('student-attendance', views.studentAttendance),
    path('student-announcement', views.studentAnnouncement),
    path('student-feesManagement', views.studentFeeManagement),
    path('final-results', views.finalResults),
    path('edit-profile', views.editProfile),
    path('update-profile', views.updateProfile),
]