from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!") # This is the simplest view possible in Django. It takes a request object and returns a response object. This response is a simple HTTP response with the text "Hello World!".