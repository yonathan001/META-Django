from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")


def homepage(request):
   return HttpResponse("This is the homepage of the website")