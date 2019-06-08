from django.shortcuts import render
from .models import Img
# Create your views here.
def uploadImg(request): # 图片上传函数
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
    return render(request, 'imgupload.html')
