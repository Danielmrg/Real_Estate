from django.db import models

# Create your models here.

class company(models.Model):
    phone = models.CharField(max_length=12,verbose_name='شماره تلفن')
    address = models.CharField(max_length=100,verbose_name='ادرس')
    email = models.EmailField(verbose_name='ایمیل')
    bio = models.TextField(verbose_name='توضیحات')
    