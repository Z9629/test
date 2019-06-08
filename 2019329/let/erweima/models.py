from django.db import models

# Create your models here.
class Coal(models.Model):
    coal_name = models.CharField(max_length=32,null=False)
    coal_img = models.ImageField(upload_to='images')
