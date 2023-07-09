from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()
    avatar = models.ImageField()

class Teacher(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()
    progamming_language = models.CharField(max_length=40)
    avatar = models.ImageField()
    class Gender(models.TextChoices):
        male = '1', 'male'
        female = '2', 'female'
        other = '3', 'other'
    gender = models.CharField(
        max_length=2,
        choices = Gender.choices,
        default = Gender.male
    )

class Courses(models.Model):
    name = models.CharField(max_length=25)
    course_number = models.IntegerField()
