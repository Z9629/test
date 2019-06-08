# login/admin.py

from django.contrib import admin
from myapp import models
from django.shortcuts import render_to_response
from django.shortcuts import render,redirect
import os


admin.site.register(models.User)
admin.site.register(models.IMG)
admin.site.register(models.GYS)

admin.site.site_header = '个性二维码'

