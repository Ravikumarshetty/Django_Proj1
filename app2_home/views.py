from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainWindow(Request):
    return HttpResponse("<h1> Link to registration page </h1> <br> <h1> Link to home page </h1>")
