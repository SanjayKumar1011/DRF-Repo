from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def student(request):
    student=[
        {'id': 1, 'name': 'Sam' , 'class' : 'CSE'}
    ]
    return HttpResponse(student)
