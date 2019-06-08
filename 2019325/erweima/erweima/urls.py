# """erweima URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from project import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path(r'hello/',views.hello),
# ]


from django.conf.urls import url
from django.contrib import admin
# from home import views as homeViews
from project import views
# from erweima.project import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^upload_avatar/', views.upload_avatar),  # 上传头像
    # url(r'^test/', views.test),  # 上传头像
    url(r'^user/', views.uss),  # 上传头像
    url(r'^userInfor/', views.userInfor),  # 上传头像
    # url(r'^test/', homeViews.test),  # 测试页面


]