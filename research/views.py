from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request):
    new_name = request.POST.get('name', 'empty')
    student = Student(name = new_name)
    student.save()
    return HttpResponse("new students created: " + request.body)

def response(request):
    answer = request.POST.get('answer')
    studentName = request.POST.get('name')
    student = Student.objects.get(name=studentName)
    student.response_set.create(answer=answer)
    return HttpResponse("response saved");
