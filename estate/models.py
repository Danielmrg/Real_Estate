from datetime import datetime as time
from django.utils import timezone
from django.urls import reverse
from django.db import models

class AreaManager(models.Manager):
    # manager for Area
    def active(self):
        return self.filter(status='a')

class Area(models.Model):
    Status = [
        ['a','فعال'],
        ['d','غیرفعال']
    ]
    title = models.CharField(max_length=120,verbose_name='نام منطقه',blank=False,null=False,unique=True)
    slug = models.SlugField(max_length=120,verbose_name='لینک',blank=False,null=False,unique=True,default='')
    code = models.IntegerField(null=False,blank=False,verbose_name='کد منطقه')
    status = models.CharField(max_length=1,choices=Status,default='d',verbose_name='وضعیت')
    objects = AreaManager()

    def get_estate(self):
        return self.area_estate.active()
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('code',)
        verbose_name ='منطقه'
        verbose_name_plural ='منطقه ها'

class EstateManager(models.Manager):
    # manager for Estate
    def active(self):
        return self.filter(state='a') 

class Estate(models.Model):
    Status = [
        ['a','فعال'],
        ['d','غیرفعال']
    ]
    title = models.CharField(max_length=225,blank=False, null=False,unique=True,verbose_name='نام بنگاه')
    slug = models.SlugField(max_length=225,verbose_name='لینک',blank=False,null=False,unique=True,default='')
    code = models.CharField(max_length=25,null=False,blank=False,verbose_name='کد بنگاه')
    status = models.CharField(max_length=1,choices=Status,default='d',verbose_name='وضعیت')
    date_make = models.DateTimeField(auto_now_add=True,null=True,verbose_name='زمان تشکیل')
    address = models.CharField(max_length=225,blank=True,null=True,verbose_name='ادرس')
    area = models.ManyToManyField(to=Area,related_name='area_estate',verbose_name='انتخاب منطقه')
    objects = EstateManager()

    def get_area(self):
        return self.area.active()
    
    def get_users(self):
        return self.estate_user.all()
    
    def get_admin(self):
        return self.estate_user.status_admin()
    
    def get_novice(self):
        return self.estate_user.status_novice()
        
    def get_address(self):
        if self.address:
            return str(self.address)
        else:
            return str(self.title)
    
    def get_advert_active(self):
        return self.estate_advertising.active()

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ('code','-date_make')
        verbose_name ='بنگاه'
        verbose_name_plural ='بنگاه ها'

