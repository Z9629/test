from django.db import models

# Create your models here.
class Classes(models.Model):
    caption = models.CharField(max_length=32)

class Student(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32,null=True)
    cls = models.ForeignKey('Classes',on_delete=None)

class Teacher(models.Model):
    name = models.CharField(max_length=32)
    cls = models.ManyToManyField('Classes') #这里会自动生成第三张表


class Administrator(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)