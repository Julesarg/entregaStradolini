from django import forms

class CourseForm(forms.Form):
    name = forms.CharField(max_length=30)
    course_number = forms.IntegerField()

class StudentForm(forms.Form):
    name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    username = forms.CharField(max_length=10)
    email = forms.EmailField()
    age = forms.IntegerField()
    avatar = forms.ImageField()

class TeacherForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    age = forms.IntegerField()
    progamming_language = forms.CharField()
    avatar = forms.ImageField()