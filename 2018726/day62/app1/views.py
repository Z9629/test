from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello!</h1>')