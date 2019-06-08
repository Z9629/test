# from django.shortcuts import render
#
# # Create your views here.
# def hello(request):
#     context = {}
#     context['hello'] = 'hello world!'
#     return render(request,'index.html',context)
#
#############################################################################################
#https://www.jb51.net/article/118632.htm

# from django.shortcuts import render, HttpResponse
# import os
# import time
# import json
#
# def test(request):
#     if request.method=='POST':
#         file_obj = request.FILES.get('avatar')
#         print('-' * 20)
#         print(file_obj)
#         return HttpResponse('sss')
#     return render(request, 'test.html')
#
#
# def upload_avatar(request):
#     time.sleep(1)
#     file_obj = request.FILES.get('avatar')
#     print('-'*20)
#     print(file_obj)
#     file_path = os.path.join(r'C:\Users\14813\Desktop\zhaopian', file_obj.name)
#     print(file_path)
#     with open(file_path, 'wb') as f:
#         for chunk in file_obj.chunks():
#             f.write(chunk)
#     return HttpResponse(file_path)




#####################################################
#https://blog.csdn.net/kaikai136412162/article/details/79110327
from django.shortcuts import render
import os
from project import models
from PIL import Image


# Create your views here.

def uss(req):
    img = models.UserInfor.objects.all()
    return render(req, 'list.html', {'img': img})


def userInfor(req):
    if req.method == "POST":
        u = req.POST.get("username", None)
        s = req.POST.get("sex", None)
        e = req.POST.get("email", None)
        p = req.POST.get("tt",None)
        print('#################################')
        print(u,s,e)
        print(os.path.abspath(p))
        print(p)
        im = Image.open(os.path.abspath(p))
        cp = im.copy()
        cp.save('./p')

        # ---------表中插入数据方式一
        # info={"username":u,"sex":s,"email":e}
        # models.UserInfor.objects.create(**info)

        # ---------表中插入数据方式二
        models.UserInfor.objects.create(
            username=u,
            sex=s,
            email=e,
            photo=p,
        )

        info_list = models.UserInfor.objects.all()

        return render(req, "list2.html", {"info_list": info_list})

    return render(req, "list2.html")