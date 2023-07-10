from django.urls import path
from mainApp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('teachers',views.teachers, name='teachers'),
    path('students',views.students, name='students'),
    path('courses',views.courses, name='courses'),
    path('errorMessage', views.errorMessage, name='errorMessage'),
    path('notInDb', views.notInDb, name='notInDb'),
    path('searchCourse/', views.searchCourse),
    path('searchStudent/', views.searchStudent),
    path('searchTeacher/', views.searchTeacher),
]
