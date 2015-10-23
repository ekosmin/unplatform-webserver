from django.db import models

# Create your models here.

class Student (models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return self.name

class Response (models.Model):
  student = models.ForeignKey(Student)
  answer = models.CharField(max_length=50)
  def __str__(self):
    return self.answer
