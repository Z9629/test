# login/views.py

from django.shortcuts import render,redirect
from myapp import models
from myapp import forms
import hashlib
# from myapp.models import IMG
import os

from django.contrib.auth.models import User
from django.shortcuts import render_to_response

from MyQR import myqr
#密码加密
def hash_code(s, salt='mysite'):# 加点盐
    h = hashlib.sha256()    #以sha256()方法加密
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()    #以16进制形式返回加密内容

def index(request):
    if request.method == 'POST':
        if request.FILES.get('img'):
            new_img = models.IMG(
                img=request.FILES.get('img'),
                name = request.FILES.get('img',None).name,
                text = request.POST.get('text'),
            )
            new_img.save()
            return redirect(showImg)

            print("##################################")
            print(new_img.text)
    zan = C_J()
    # print(C_J())
    # zan = models.GYS.objects.all()
    # print('zan', zan)
    # for m in zan:
    #     m.pic_img = r'../media/'+m.pic_img.name
    #     print(m.pic_img)
    return render(request,'index.html',{'list':zan})

def login(request):
    zan = C_J()
    # print(C_J())
    # zan = models.GYS.objects.all()
    # print('zan', zan)
    # for m in zan:
    #     m.pic_img = r'../media/' + m.pic_img.name
    #     print(m.pic_img)
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)   #获取每个input标签
        message = "请检查填写的内容！"
        if login_form.is_valid():       #这个就是用于验证输入表单内容的合法性
            username = login_form.cleaned_data['username']      #cleaned_data会将input标签中的变量和值作为以字典的一个元素形式表现出来
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    print("##############################################")
                    print(user.name)
                    return redirect('/index/')
                else:
                    message = "密码不正确！"

            except:
                message = "用户不存在！"
        return render(request, 'login.html', {'login_form':login_form,'list':zan,'message':message})

    login_form = forms.UserForm()

    return render(request, 'login.html', {'login_form':login_form,'list':zan})

def register(request):
    zan = C_J()
    # print(C_J())
    # zan = models.GYS.objects.all()
    # print('zan', zan)
    # for m in zan:
    #     m.pic_img = r'../media/' + m.pic_img.name
    #     print(m.pic_img)
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']     #cleaned_data会将input标签中的变量和值作为以字典的一个元素形式表现出来
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', {'register_form':register_form,'list':zan,'message':message})
            else:
                ## 匹配，对应SQL：select * from User where name = 'username'
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', {'register_form':register_form,'list':zan,'message':message})
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html',  {'register_form':register_form,'list':zan,'message':message})

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = forms.RegisterForm( initial={'sex': 'male'})


    return render(request, 'register.html', {'register_form':register_form,'list':zan})

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']

    return redirect("/index/")




# Create your views here.
# @csrf_exempt


# @csrf_exempt
def showImg(request):
    # queryset = models.Classes.objects.all(),  # 利用queryset连接数据库，只能连接object类型
    imgs = models.IMG.objects.all()
    # print(type(imgs))
    #重复覆盖，取最后一张图片
    for i in imgs:
        t = i


    now = os.path.abspath('.')  #C:\Users\14813\Desktop\python\2019330(2)\test5
    print("now:"+now)
    pictures = now + t.img.url
    save_dirs = now + '\\media\\imgs'
    print('save:',save_dirs)
    print(t.name)

    #生成个性二维码操作
    myqr.run(
        words=t.text,
        # picture= '..'+ t.img.url,
        picture  = pictures,
        colorized=True,
        # version=1,
        save_name= t.name,
        save_dir=save_dirs,
    )



    content = {}
    # content['t'] = b
    # content['t'] = os.path.abspath(r'../') +t.img.url
    content['t'] = r'../media/imgs/' + t.name
    content['n'] = t.name
    print(content['t'])
    print(content['n'])
    zan = C_J()
    # print(C_J())
    # zan = models.GYS.objects.all()
    # print('zan', zan)
    # for m in zan:
    #     m.pic_img = r'../media/' + m.pic_img.name
    #     print(m.pic_img)
    return render(request, 'show.html',{'list':zan,'t':content['t'],'n':content['n']})

#
#定义函数，实现轮播图
def C_J():
    zan = models.GYS.objects.all()
    print('zan', zan)
    for m in zan:
        m.pic_img = r'../media/' + m.pic_img.name
        # print(m.pic_img)
    return zan

#
# def ZANZHU(request):
#     if request.method == 'POST':
#         new_img1 = models.GYS(
#             pic_img = request.FILES.get('img1',None),
#             pic_name = request.POST.get('name1',None),
#             pic_lj = request.POST.get('href1',None),
#         )
#
#         # models.GYS.objects.create(
#         #     pic_img=u,
#         #     pic_name=s,
#         #     pic_lj=e,
#         # )
#
#         # info_list = models.GYS.objects.all()
#         #
#         # return render(request, "upload.html", {"list": info_list})
#
#
#
#         new_img1.save()
#         zan = models.GYS.objects.all()
#         for m in zan:
#             print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#             print(m.pic_img)
#             m.pic_img = r'../media/' + m.pic_img.name
#             print(m.pic_img)
#         for p in zan:
#             print(p.pic_img)
#
#         return render(request, 'base.html', {"list": zan})
#     return render(request, 'upload.html')
#
#
# def zs(request):
#     # imgs1 = models.GYS.objects.all()  # img = imgs[-1]
#     zan = models.GYS.objects.all()
#     for m in zan:
#         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#         print(m.pic_img)
#         m.pic_img = r'../media/'+m.pic_img.name
#         print(m.pic_img)
#     for p in zan:
#         print(p.pic_img)
#
#     return render(request, 'base.html',{"list":zan})
#
