from django.db import models

# Create your models here.
# class Person(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.IntegerField()
#
#     # def __unicode__(self):
#     # 在Python3中使用 def __str__(self):
#     def __str__(self):
#         return self.name
#
# class IMG(models.Model):
#     image = models.ImageField(upload_to='image')
#     name = models.CharField(max_length=20)
#     def __str__(self):
#     # 在Python3中使用 def __str__(self):
#         return self.name


################################################
#上传图片的模型类
class Pictures(models.Model):
    pic = models.ImageField(upload_to='booktest/')
    def __str__(self):
        return self.pic