from django.urls import path
from smsAuth import views


urlpatterns = [
    path('create-management-account', views.createManageAccount),
    path('create-student-account', views.createStudentAccount),
    path('create-student-account-auth', views.createStudentAccountAuth),
    path('create-management-account-auth', views.createManagementAccountAuth),
    path('user-auth', views.userAuthentication),
    path('', views.userLogin),
    path('logout', views.userLogout),
    path('reset-password', views.resetPassword),
    path('reset-password-auth', views.resetPasswordAuth),

]