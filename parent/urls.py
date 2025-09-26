from django.urls import path
from parent import views


urlpatterns = [
    path('parent-profile', views.parentProfile),
    path('parent-attendance', views.parentAttendance),
    path('parent-results', views.parentResults),
     path('edit-parent-profile', views.editParentProfile),
    path('update-parent-profile', views.updateParentProfile),

]