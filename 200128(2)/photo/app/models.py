from django.db import models

# Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=50)
#
#     body = models.TextField()
#     created_time = models.DateTimeField()
#     modified_time = models.DateTimeField()
#     experpt = models.CharField(max_length=200)
#     category = models.ForeignKey('Category', on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Tag)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     img = models.ImageField(upload_to='./img/', blank=True, null=True)      # 添加的img
#
#
# def __str__(self):
#     return self.title


class IMG(models.Model):
    img = models.ImageField(upload_to='./img/',blank=True, null=True)