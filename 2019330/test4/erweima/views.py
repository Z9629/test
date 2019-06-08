from django.shortcuts import render
# from erweima.models import Person,IMG
# Create your views here.
# def hello(request):
#     IMG.objects.filter(name='bg')
#     image = IMG.objects.all()
#     return render(request, 'Welcome.html',{'image':image})

# 上传图片
from django.conf import settings
from .models import Pictures
# 返回上传图片的页面
def getUpload(request):
    return render(request,'templates/upload.html')

#　发来表单　实现上传功能
def upload(request):
    # 从请求当中　获取文件对象
    f1 = request.FILES.get('picture')
    #　利用模型类　将图片要存放的路径存到数据库中
    p = Pictures()
    p.pic = "booktest/" + f1.name
    p.save()
    # 在之前配好的静态文件目录static/media/booktest 下 新建一个空文件
    # 然后我们循环把上传的图片写入到新建文件当中
    fname = settings.MEDIA_ROOT + "/booktest/" + f1.name
    with open(fname,'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    return HttpResponse("上传成功")