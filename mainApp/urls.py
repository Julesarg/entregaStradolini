from django.urls import path
from mainApp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('teachers',views.teachers, name='teachers'),
    path('students',views.students, name='students'),
    path('courses',views.courses, name='courses'),
]
