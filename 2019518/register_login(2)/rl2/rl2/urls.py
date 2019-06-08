"""rl2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# mysite_login/urls.py

# from django.conf.urls import url,include
# from django.contrib import admin
# from myapp import views
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^index/', views.index),
#     url(r'^login/', views.login),
#     url(r'^register/', views.register),
#     url(r'^logout/', views.logout),
#
# ]


from django.conf.urls import url,include
from django.contrib import admin
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

#这个函数会遍历 INSTALLED_APPS里面的设置，发现哪里有admin.py,就会执行其中的代码
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^upload/', views.ZANZHU),
    # url(r'^zs/', views.zs),
    url(r'^show/', views.showImg),
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^$', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)