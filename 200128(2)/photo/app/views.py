from django.shortcuts import render
from . import templates
# from app import templates
from .models import IMG
# Create your views here.
def upload(request):
    return render(request, 'upload.html')
def show(request):
    new_img = IMG(img=request.FILES.get('img'))
    new_img.save()
    content = {
        'aaa': new_img,
    }
    return render(request, 'show.html', content)