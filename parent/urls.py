from django.urls import path
from parent import views


urlpatterns = [
    path('parent-profile', views.parentProfile),
    path('parent-attendance', views.parentAttendance),
    path('parent-results', views.parentResults),
    path('edit-parent-profile/<int:parent_id>', views.editParentProfile),
    path('update-parent-profile/<int:parent_id>', views.updateParentProfile),
]