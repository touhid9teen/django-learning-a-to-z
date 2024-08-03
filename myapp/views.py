from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "myapp/index.html")
# This view function takes a request object and 
# returns a response object. The response is 
# rendered using the template myapp/index.html. 
# This template is a simple HTML file that displays
#  the text "Hello, World!".


# from django.http import HttpResponse
# def index(request):
# return HttpResponse("Hello World!") 
# This is the simplest view 
# possible in Django. It takes a request object and returns a 
# response object. 
# This response is a simple HTTP response with the text "Hello World!".