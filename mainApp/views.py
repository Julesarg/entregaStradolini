from django.shortcuts import redirect, render
from django.http import HttpResponse
from mainApp.models import Course, Teacher, Student
from mainApp.forms import CourseForm, StudentForm, TeacherForm
from django.contrib import messages

def index(request):
    return render(request, 'mainApp/index.html')
def errorMessage(request):
    return render(request, 'mainApp/errorMessage.html')
def notInDb(request):
    return render(request, 'mainApp/notInDb.html')

#CARGAR FORMULARIOS#
#cursos#
def courses(request):
    if request.method == "POST":
        myForm = CourseForm(request.POST)
        print(myForm)
        if myForm.is_valid():
            inf = myForm.cleaned_data
            course = Course(name = inf['name'], course_number = inf['course_number'])
            course.save()
            messages.success(request, f'Course: {course.name.capitalize()} - Course Number: {course.course_number}')
        return render(request, 'mainApp/index.html')
    else:
        myForm = CourseForm()
    return render(request, 'mainApp/courses.html', {'myForm': myForm})
#estudiantes#
def students(request):
    if request.method == "POST":
        myForm = StudentForm(request.POST, request.FILES)
        print(myForm)
        if myForm.is_valid():
            inf = myForm.cleaned_data
            student = Student(name = inf['name'], last_name = inf['last_name'], username = inf['username'], email = inf['email'], age = inf['age'], avatar = inf['avatar'])
            student.save()
            messages.success(request,f'Student "{student.name.capitalize()} {student.last_name.capitalize()}"')
        return render(request, 'mainApp/index.html')
    else:
        myForm = StudentForm()
    return render(request, 'mainApp/students.html', {'myForm': myForm})
#profesores#
def teachers(request):
    if request.method == "POST":
        myForm = TeacherForm(request.POST, request.FILES)
        print(myForm)
        if myForm.is_valid():
            inf = myForm.cleaned_data
            teacher = Teacher(name = inf['name'], last_name = inf['last_name'], username = inf['username'], email = inf['email'], age = inf['age'], programming_language = inf['progamming_language'], avatar = inf['avatar'])
            teacher.save()
            messages.success(request, f'Teacher "{teacher.name.capitalize()} {teacher.last_name.capitalize()}" for {teacher.programming_language}')
        return render(request, 'mainApp/index.html')
    else:
        myForm = TeacherForm()
    return render(request, 'mainApp/teachers.html', {'myForm': myForm})

#CARGAR BUSQUEDAS#
#de cursos#
def searchCourse(request):    
    if request.GET['course_number']:
        course_number = request.GET['course_number']
        course = Course.objects.filter(course_number__icontains=course_number)
        if course:
            return render(request, 'mainApp/index.html', {'course': course, 'course_number': course_number})
        elif not course:
            return render(request, 'mainApp/notInDb.html')
        else:
            return render(request, 'mainApp/index.html')
    else:
        return render(request,'mainApp/errorMessage.html')
#de estudiantes#
def searchStudent(request):
    if request.GET['username']:
        username = request.GET['username']
        student = Student.objects.filter(username__icontains=username)
        if student:
            return render(request, 'mainApp/index.html', {'student': student, 'username': username})
        elif not student:
            return render(request, 'mainApp/notInDb.html')
        else:            
            return render(request, 'mainApp/index.html')
    else:
        return redirect('../errorMessage')
#de profesores#    
def searchTeacher(request):
    if request.GET['username']:
        username = request.GET['username']
        teacher = Teacher.objects.filter(username__icontains=username)
        if teacher:
            return render(request, 'mainApp/index.html', {'teacher': teacher, 'username': username})
        elif not teacher:
            return render(request, 'mainApp/notInDb.html')
        else:            
            return render(request, 'mainApp/index.html')
    else:
        return redirect('../errorMessage')