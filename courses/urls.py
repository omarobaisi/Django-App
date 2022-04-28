from django.urls import path
from courses import views

urlpatterns = [
    path('', views.courses_index, name='courses_index'),
    path('<int:pk>/', views.courses_detail, name='courses_detail'),
    path('teacher/<int:pk>', views.teacher_detail, name='teacher_detail'),
    path('student/<int:pk>', views.student_detail, name='student_detail'),
]