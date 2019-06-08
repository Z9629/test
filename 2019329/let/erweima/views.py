from django.shortcuts import render

# Create your views here.
def he(request):
    context = {}
    context['hello'] = 'hello world!'
    return render(request,'index.html',context)