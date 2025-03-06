from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   path = request.path
   response = HttpResponse("this response is coming from the view")
   return response


def menuitems(request, dishes):
     items = {
            'burger': 'burger is a fast food',
            'pizza': 'pizza is an italian food',
            'pasta': 'pasta is a chinese food',
            'noodles': 'noodles is a chinese food',
            'sandwich': 'sandwich is a fast food',
     }

     discription = items[dishes]
     return HttpResponse(f" <h2> {dishes} </h2>"+ discription)