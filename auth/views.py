from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Home")
def login(request):
    return HttpResponse("Login Page")
def register(request):
    return HttpResponse("Register Page")