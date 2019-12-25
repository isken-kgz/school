from django.db import models

from datetime import datetime


# Create your models here.

class CourseInstructor(models.Model):
    courseID = models.ForeignKey('Course', on_delete=models.CASCADE)
    personID = models.ForeignKey('Person', on_delete=models.CASCADE)


class Person(models.Model):
    personID = models.IntegerField()
    lastName = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    hireDate = models.DateTimeField(default=datetime.now(), blank=True)


class Course(models.Model):
    courseID = models.IntegerField()
    Title = models.CharField(max_length=255)
    Credits = models.IntegerField()
    departmentID = models.ForeignKey('Department', on_delete=models.CASCADE)


class Department(models.Model):
    departmentID = models.IntegerField()
    name = models.CharField(max_length=255)
    budget = models.IntegerField()
    startdate = models.IntegerField
    administrator = models.CharField(max_length=255)


class OfficeAssigment(models.Model):
    instructorID = models.IntegerField()
    location = models.CharField(max_length=255)
    timeStamp = models.IntegerField()


class StudentGrade(models.Model):
    enrollmentID = models.IntegerField()
    courseID = models.ForeignKey('Course', on_delete=models.CASCADE)
    studentID = models.ForeignKey('Person', on_delete=models.CASCADE)
    grade = models.CharField(max_length=255)


class OnlineCourse(models.Model):
    courseID = models.ForeignKey('Course', on_delete=models.CASCADE)
    url = models.URLField(max_length=200)


class OnsiteCourse(models.Model):
    courseID = models.ForeignKey('Course', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    days = models.IntegerField()
    time = models.IntegerField()
