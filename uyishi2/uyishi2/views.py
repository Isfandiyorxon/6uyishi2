from django.core.handlers.wsgi import WSGIRequest
from  django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from  django.shortcuts import render

def home(request:WSGIRequest):
    return render(request,'home.html')

def help(request:WSGIRequest):
    return render(request,'help.html')

def login(request:WSGIRequest):
    return  render(request,'login.html')

def about(request:WSGIRequest):
    return render(request,'about.html')

def add(request:WSGIRequest):
    return render(request,'add.html')

def update(request:WSGIRequest):
    return render(request,'update.html')

def services(request:WSGIRequest):
    return render(request,'serxcices.html')

def contact(request:WSGIRequest):
    return render(request,'contact.html')

def current(request:WSGIRequest):
    return render(request,'Curent Statistics.html')

def delate(request:WSGIRequest):
    return render(request,'delate.html')