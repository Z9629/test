# Create your views here.
from django.shortcuts import render,redirect
from img_db.models import IMG
import os
from MyQR import myqr
# Create your views here.
# @csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name = request.FILES.get('img').name,
            text = request.POST.get('text')
        )
        text = request.POST.get('txt')
        print(text)
        new_img.save()
        return redirect(showImg)
        print("##################################")
        print(new_img.text)
        # print(request.FILES.get('img'))
        # def __init__(self, *args, **kwargs):  # 自定义__init__
        #     super(uploadImg, self).__init__(*args, **kwargs)  # 调用父类的__init__

            # self.fields['t2c'].choices = models.Classes.objects.values_list('id', 'title')  # 为字段t2c的choices赋值
    return render(request, 'upload.html')


# @csrf_exempt
def showImg(request):
    # queryset = models.Classes.objects.all(),  # 利用queryset连接数据库，只能连接object类型
    imgs = IMG.objects.all()   # img = imgs[-1]
    # print(type(imgs))
    #重复覆盖，取最后一张图片
    for i in imgs:
        t = i
    # print('###############@@@@@@@@@@@@@@@')
    # print(t.img.url)
    # print(imgs)

    #
    # content = {}
    # content['t'] = t.img.url


    # p = t.img.url
    # print('##########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # print(content['t'])
    # for i in imgs:
    #     # print (i.img.url)
    #     t = os.path.abspath(i.img.name)
    #     print(os.path.abspath(i.img.name))
    #     print()
    # print(t.name)
    print('$$$$$$$$$$$$#############$$$$$$$$$$$$$$')

    # x = os.path.abspath('../')+ t.img.url
    # print(x)        #C:\Users\14813\Desktop\python\2019330(2)/media/img/3.gif
    # print(t.name)   # wm.jpg
    # print(t.img.name)  # img/wm.jpg
    # time.sleep(1)
    # print(t.img.url)
    # picture = os.path.join(r'../',t.img.url)  #/media/img/1_FiZLWld.png

    # picture = r'..' + t.img.url     #../media/img/2_Nrf0TSL.gif
    # print('#$%^%^&&&*')
    # print(picture)
    # print(os.path.abspath('.'))     #C:\Users\14813\Desktop\python\2019330(2)\test5

    now = os.path.abspath('.')  #C:\Users\14813\Desktop\python\2019330(2)\test5
    # print('******',type(now))
    # print(now + t.img.url)
    pictures = now + t.img.url
    save_dirs = now + '\\media\\imgs'
    print('save:',save_dirs)
    print(t.name)
    # picture = os.path.join(now,t.img.url)   #C:/media/img/wm.jpg
    # print('#$%^&*')
    # print(now)
    # print('t.img',t.img)
    # print(type(t.img.url))
    # print(t.img.url)
    # print(os.path.abspath(t.img.url))
    # print(os.path.abspath(t.img))
    # print(picture)
    # print(os.path.abspath(t.img.url))   #C:\media\img\wm.jpg
    # print(t.img.url)
    myqr.run(
        words='http://www.baidu.com',
        # picture= '..'+ t.img.url,
        picture  = pictures,
        colorized=True,
        save_name= t.name,
        save_dir=save_dirs,
    )
    # time.sleep(1)
    # myqr.run(
    #     words = 'ttplogin',
    #     # picture=t.img.url,
    #     picture = t.img.url,
    #     # colorized=True,
    #     # save_name=t.name,
    # #     # save_dir=os.path.abspath('../media/imgs'),
    # #     save_dir='../media/imgs',
    # )

    # a = r'../meida/img'
    # print('#########@@@@@@@@@@@!!!!!!!!!!!!!!')
    # print('a'+ a)
    # b = os.path.join(a, t.name)
    # print('b'+ b)
    # print(os.path.abspath('../')+ t.img.url)
    # print(t.img.url)



    content = {}
    # content['t'] = b
    # content['t'] = os.path.abspath(r'../') +t.img.url
    content['t'] = r'../media/imgs/' + t.name
    content['n'] = t.name
    print(content['t'])
    return render(request, 'show.html',content)


# def qr(w,p,c_t,c_f,s_n,s_d):
#     myqr.run(
#         words=w,
#         picture=p,
#         colorized=c,
#         save_name=s_n,
#         save_dir=s_d,
#     )






