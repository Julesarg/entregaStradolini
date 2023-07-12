from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f'Name: {self.name}, Lastname: {self.last_name}, Username: {self.username}, Email: {self.email}, Age: {self.age}, Profile Pic: {self.avatar}'

class Teacher(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()
    programming_language = models.CharField(max_length=40)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f'Name: {self.name}, Lastname: {self.last_name}, Username: {self.username}, Email: {self.email}, Age: {self.age}, Programming Language: {self.programming_language}, Profile Pic: {self.avatar}'

class Course(models.Model):
    name = models.CharField(max_length=25)
    course_number = models.IntegerField()

    def __str__(self):
        return f'Course Name: {self.name} - Course Number: {self.course_number}'
