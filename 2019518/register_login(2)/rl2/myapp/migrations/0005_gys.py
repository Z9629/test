# Generated by Django 2.0.4 on 2019-04-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_delete_img2'),
    ]

    operations = [
        migrations.CreateModel(
            name='GYS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_img', models.ImageField(upload_to='pic')),
                ('pic_name', models.CharField(max_length=200)),
                ('pic_lj', models.CharField(max_length=200)),
            ],
        ),
    ]