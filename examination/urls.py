from django.urls import path
from examination import views


urlpatterns = [
    path('manage-exam', views.manageExam),
    path('save-exam-results', views.saveExamResults),
    path('edit-exam-results', views.editExamResults),
    path('update-exam-results', views.updateExamResults),
]