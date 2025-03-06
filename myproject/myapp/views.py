from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   path = request.path
   response = HttpResponse("this response is coming from the view")
   return response


def 