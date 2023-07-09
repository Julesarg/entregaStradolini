from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mainApp/index.html')

def students(request):
    return render(request, 'mainApp/students.html')

def courses(request):
    return render(request, 'mainApp/courses.html')

def teachers(request):
    return render(request, 'mainApp/teachers.html')