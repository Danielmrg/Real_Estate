from django.contrib.auth.models import AbstractUser,BaseUserManager
from estate.models import Estate
from django.db import models


class UserManager(BaseUserManager):
    # manage user
    def status_novice(self):
        return self.filter(novice=True)
    
    def status_admin(self):
        return self.filter(admin=True)

    def active(self):
        return self.filter(status='a')


class User(AbstractUser):
    Status=[
        ['a','فعال'],
        ['d','غیرفعال']
    ]
    email = models.EmailField(blank=False, null=False,verbose_name='ایمیل',unique=True)
    number = models.CharField(max_length=12,verbose_name='شماره تلفن',blank=False,null=False,default='09')
    status = models.CharField(choices=Status,max_length=1,default='d',blank=False,null=False,verbose_name='وضعیت کاربر')
    admin = models.BooleanField(default=False,verbose_name='مدیر بنگاه',help_text='مدیر یا مدیران بنگاه ')
    novice = models.BooleanField(default=True,verbose_name='تازه کار')
    estate = models.ForeignKey(to=Estate, related_name='estate_user', null=True, verbose_name='بنگاه', on_delete=models.SET_NULL)
    objects = UserManager()
    
    def get_status(self):
        return self.status

    def get_estate(self):
        return self.estate
        
    def __str__(self):
        return self.username
    
    def get_all_advertising(self):
        return self.user_advertising.all()

    def get_active_advertising(self):
        return self.user_advertising.active()

    def get_deactivate_advertising(self):
        return self.user_advertising.deactivate()

