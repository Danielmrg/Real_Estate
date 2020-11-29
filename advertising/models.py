from django.utils.html import format_html
from datetime import datetime as time
from django.utils import timezone
from estate.models import Estate
from account.models import User
from django.urls import reverse
from django.db import models


class CategoryManager(models.Manager):
    # manager for categories

    def active(self):
        return self.filter(status='a')

class Category(models.Model):
    Status = [
        ['a','فعال'],
        ['d','غیرفعال']
    ]
    title = models.CharField(max_length=100,verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100,verbose_name='لینک')
    status = models.CharField(max_length=1,choices=Status,default='d',verbose_name='وضعیت')
    objects = CategoryManager()

    def get_advertising(self):
        return self.category_advertising.active()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='دسته بندی'
        verbose_name_plural ='دسته بندی ها'

class AdvertisingManager(models.Manager):
    # manager for advertising's
    def active(self):
        return self.filter(status='a')

    def deactivate(self):
        return self.filter(status='d')

    def publish(self):
        return self.filter(status='a',send_in_publish=True)

    def in_estate(self):
        return self.filter(status='a',send_in_estate=True)
    def category_sale(self):
        return self.filter(category="فروش")
    

class Advertising(models.Model):
    Status = [
        ['a','فعال'],
        ['d','غیرفعال']
    ]
    image =models.ImageField(default='image_default/default.jpg',blank=True,upload_to='image-advertising/',verbose_name='عکس')
    title = models.CharField(max_length=225,blank=False,null=False,verbose_name='عنوان آگهی')
    price = models.FloatField(null=True,blank=True,verbose_name='قیمت')
    slug = models.SlugField(max_length=225,unique=True,blank=True,null=True,verbose_name='لینک')
    address = models.CharField(max_length=225,blank=True,null=True,verbose_name='ادرس')
    description = models.TextField(max_length=1000,blank=False,null=False,verbose_name='توضیحات')
    status = models.CharField(max_length=1,choices=Status,default='d',verbose_name='وضعیت')
    date_added = models.DateTimeField(auto_now_add=True,null=True,verbose_name='زمان انتشار')
    send_in_estate = models.BooleanField(default=False,verbose_name='ارسال در گروه بنگاه')
    send_in_publish = models.BooleanField(default=False,verbose_name='ارسال به صورت عمومی')
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE,related_name='category_advertising',verbose_name='دسته بندی')
    user = models.ForeignKey(to=User,related_name='user_advertising',on_delete=models.CASCADE,verbose_name='اگهی دهنده')
    estate = models.ForeignKey(to=Estate,related_name='estate_advertising',null=True,on_delete=models.CASCADE,verbose_name='بنگاه')
    objects=AdvertisingManager()
    def get_status(self):
        if self.status =='a':
            return True
        else:
            return False
    get_status.boolean=True
    def get_category(self):
        return self.category

    def get_user(self):
        return self.user
    
    def get_image(self):
        return self.image.url
    
    def get_image_for_admin(self):
        return format_html(f'<img style="width:150px; height:80px;" src="{self.image.url}">')
    get_image_for_admin.short_description ='عکس'

    def get_all_images(self):
        return self.advertising_images.all()
    
    def get_address(self):
        if self.address:
            return str(self.address)
        else:
            return str(self.user.estate.title)

    def get_price(self):
        if self.price:
            return self.price
        else:
            return 'توافقی'
    get_price.short_description="قیمت"

    def get_absolute_url(self):
        return reverse('account:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('date_added',)
        verbose_name ='اگهی'
        verbose_name_plural ='اگهی ها'
    

class Images(models.Model):
    image = models.ImageField(default='image_default/default.jpg',blank=True,null=True,upload_to='images-adv/',verbose_name='عکس')
    advertising = models.ForeignKey(to=Advertising,on_delete=models.CASCADE,related_name='advertising_images',verbose_name='اگهی')
    
    def get_image(self):
        return self.image.url