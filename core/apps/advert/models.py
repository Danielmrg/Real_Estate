import os
import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.utils.html import format_html
from django.db.models import Q
from django.http import Http404
from django.urls import reverse
from authentication.models import User
from autoslug import AutoSlugField

def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return  name , ext

def change_file_name(instance, filename):
    name,ext = get_file_ext(filename)
    new_name = f"Poster/{instance.id}-{instance.title}{ext}"
    return new_name




class AdvertQuerySet(models.QuerySet):
    pass

class AdvertManager(models.Manager):
    def get_queryset(self):
        return AdvertQuerySet(self.model, using=self._db)
    
    def active(self):
        return self.filter(is_active=True)
    
    def public(self):
        return self.filter(is_public=True,is_active=True)
    
    def search(self,keyword):
        lookup = (
            Q(title__icontains=keyword)|
            Q(detail__icontains=keyword)
        )
        return self.filter(lookup,is_active=True,is_public=True).distinct() 
        # return advert    

    def get_object_or_pass(self,Uid):
        data = self.filter(Uid=Uid)
        if data != None and data.count() < 2:
            return data.first()
        return None
    
class Advert(models.Model):
    choices_status = [
        ('1','فروش'),
        ('2','رهن'),
        ('3','اجاره')
    ]
    choices_housetype = [
        ('1','ویلایی'),
        ('2','آپارتمانی'),
        ('3','زمین'),
        ('4','سایر موارد')
    ]
    choices_statustype = [
        ('1','تجاری'),
        ('2','مسکونی')
    ]
    choices_count = [
        ('1','1-2'),
        ('2','3-4'),
        ('3','5-6'),
    ]
    Uid = models.UUIDField(max_length=12,default=uuid.uuid4,editable=False,unique=True)
    title = models.CharField(max_length=50,null=False,blank=False,verbose_name='عنوان')
    slug = AutoSlugField(populate_from='title')
    poster = models.ImageField(upload_to=change_file_name,default='image_default\default.jpg',blank=False, null=False,verbose_name='پستر')
    detail = models.CharField(max_length=80,null=False,blank=False,verbose_name='جزئیات')
    price = models.IntegerField(null=True,blank=True,verbose_name='قیمت')
    area = models.CharField(max_length=150,verbose_name='متراژ',blank=False, null=False)
    stat = models.CharField(max_length=150,verbose_name='منطقه')
    address = models.TextField(verbose_name="ادرس",blank=True,null=True)
    beds = models.CharField(choices=choices_count,max_length=1,default='1',verbose_name="اتاق خواب",null=False,blank=False)
    baths = models.CharField(choices=choices_count,max_length=1,default='1',verbose_name="حمام",null=False,blank=False)
    wc = models.CharField(choices=choices_count,max_length=1,default='1',verbose_name="سرویس بهداشتی",null=False,blank=False)
    garages = models.BooleanField(default=True,verbose_name = 'پارکینگ')
    statustype = models.CharField(choices=choices_statustype,max_length=1,null=False,blank=False,default='0',verbose_name='نوع ملک')
    house_type = models.CharField(choices=choices_housetype,max_length=1,null=False,blank=False,default='0',verbose_name='نوع خانه')
    category = models.CharField(choices=choices_status,max_length=1,null=False,blank=False,default='0',verbose_name='وضعیت اگهی')
    description = models.TextField(max_length=500,blank=False, null=False,verbose_name='توضیحات')
    is_public = models.BooleanField(default=False,verbose_name='عمومی')
    year_created = models.IntegerField(verbose_name='سال ساخت')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='زمان ساخت')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='زمان اپدیت')
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name='کاربر',related_name='user_advert')
    is_active = models.BooleanField(verbose_name='فعال/غیر فعال',default=True)
    url = models.URLField(verbose_name='ادرس ویدیو',blank=True, null=True)
    options = models.ManyToManyField(to='Option',related_name='advert_option',null=True,blank=True) 
    flooring = models.CharField(verbose_name="کف پوش",max_length=50,blank=True, null=True)
    objects = AdvertManager()
    
    def get_poster(self):
        return self.poster.url
    
    def get_price_of_meter(self):
        return "{:,.0f} تومان".format(round(int(self.price)/int(self.area),2))
    
    def get_price_split(self):
        return "{:,.0f}".format(int(self.price))
    def get_gallery(self):
        return self.gallery.all()
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('home:detail-advert', kwargs={'Uid': self.Uid})
        
    def get_html_poster(self):
        return format_html(f"<img src='{self.get_poster()}' class='img-thumbnail' style='height:100px; width:300px;' alt='{self.slug}'>")
    
    
    def __str__(self):
        return f"{self.title}"
        
def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return  name , ext

def change_file_name(instance, filename):
    name,ext = get_file_ext(filename)
    new_name = f"Gallery/{instance.id}-Gallery{ext}"
    return new_name

class GalleryImage(models.Model):
    image = models.ImageField(upload_to=change_file_name,default='image_default\default.jpg',verbose_name='عکس')
    advert = models.ForeignKey(to=Advert,on_delete=models.CASCADE,related_name='gallery')
    
    def get_image(self):
        return self.image.url

class AdvertManager(models.Manager):
    def create_for_first(self,userip,advert):
        data = self.filter(user_ip=userip,advert=advert)
        if data == None:
            return self.create(user_ip = userip ,advert=advert,view = 1)
        else:
            pass
    def count_view(self):
        return self.all().count()

class AdvertView(models.Model):
    user_ip = models.CharField(max_length=150,blank=True, null=True,verbose_name='ip کاربر')
    view = models.IntegerField(default=0,verbose_name='تعداد بازدید',blank=True,null=True)
    advert = models.ForeignKey(to=Advert,on_delete=models.CASCADE,related_name='advertview',verbose_name='آگهی')
    
class Option(models.Model):
    title = models.CharField(max_length=150,verbose_name='عنوان',blank=False, null=False,unique=True)
    
    def __str__(self):
        return f"{self.title}"