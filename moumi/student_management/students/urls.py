from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/new/', views.create_student, name='create_student'),
    path('student/<int:pk>/edit/', views.update_student, name='update_student'),
    path('student/<int:pk>/delete/', views.delete_student, name='delete_student'),
]
