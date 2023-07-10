from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")

class Teacher(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()
    programming_language = models.CharField(max_length=40)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")

class Course(models.Model):
    name = models.CharField(max_length=25)
    course_number = models.IntegerField()
