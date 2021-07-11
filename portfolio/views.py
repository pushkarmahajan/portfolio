from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Project  # importing the project model

# Create your views here.


def home(request):
    projects = Project.objects.all()  # getting all the objects of the Project model
    return render(request, 'portfolio/home.html', {'projects': projects})
