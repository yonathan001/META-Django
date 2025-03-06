from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   path = request.path
   return HttpResponse(path, content_type='text/html', charset='utf-8')


def homepage(request):
   return HttpResponse("This is the homepage of the website")

def about(request):
   return HttpResponse("This is the about page of the website")