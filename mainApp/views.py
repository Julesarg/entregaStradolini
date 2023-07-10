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

# def students(request):
#     return render(request, 'mainApp/students.html')

# def courses(request):
#     return render(request, 'mainApp/courses.html')

# def teachers(request):
#     return render(request, 'mainApp/teachers.html')

def courses(request):
    if request.method == "POST":
        myForm = CourseForm(request.POST)
        print(myForm)
        if myForm.is_valid():
            inf = myForm.cleaned_data
            course = Course(name = inf['name'], course_number = inf['course_number'])
            course.save()
            messages.success(request, 'Added Succesfully')
        return render(request, 'mainApp/index.html')
    else:
        myForm = CourseForm()
    return render(request, 'mainApp/courses.html', {'myForm': myForm})

def students(request):
    if request.method == "POST":
        myForm = StudentForm(request.POST, request.FILES)
        print(myForm)
        if myForm.is_valid():
            inf = myForm.cleaned_data
            student = Student(name = inf['name'], last_name = inf['last_name'], username = inf['username'], email = inf['email'], age = inf['age'], avatar = inf['avatar'])
            student.save()
            messages.success(request, 'Added Succesfully')
        return render(request, 'mainApp/index.html')
    else:
        myForm = StudentForm()
    return render(request, 'mainApp/students.html', {'myForm': myForm})

def teachers(request):
    if request.method == "POST":
        myForm = TeacherForm(request.POST)
        print(myForm)
        if myForm.is_valid():
            inf = myForm.cleaned_data
            teacher = Teacher(name = inf['name'], last_name = inf['last_name'], username = inf['username'], email = inf['email'], age = inf['age'], progamming_language = inf['progamming_language'], avatar = inf['avatar'])
            teacher.save()
            messages.success(request, 'Added Succesfully')
        return render(request, 'mainApp/index.html')
    else:
        myForm = TeacherForm()
    return render(request, 'mainApp/teachers.html', {'myForm': myForm})

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
        return redirect('../errorMessage')
    
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