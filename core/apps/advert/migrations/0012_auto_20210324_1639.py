# Generated by Django 3.0 on 2021-03-24 12:09

import advert.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0011_auto_20210324_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='baths',
            field=models.CharField(choices=[('1', '1-2'), ('2', '3-4'), ('3', '5-6')], default='1', max_length=1, verbose_name='حمام'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='beds',
            field=models.CharField(choices=[('1', '1-2'), ('2', '3-4'), ('3', '5-6')], default='1', max_length=1, verbose_name='اتاق خواب'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='category',
            field=models.CharField(choices=[('2', 'فروش'), ('3', 'رهن'), ('4', 'اجاره')], default='0', max_length=1, verbose_name='وضعیت اگهی'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='house_type',
            field=models.CharField(choices=[('1', 'ویلایی'), ('2', 'آپارتمانی'), ('3', 'زمین'), ('4', 'سایر موارد')], default='0', max_length=1, verbose_name='نوع خانه'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='poster',
            field=models.ImageField(default='image_default\\default.jpg', upload_to=advert.models.change_file_name, verbose_name='پستر'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='statustype',
            field=models.CharField(choices=[('1', 'تجاری'), ('2', 'مسکونی')], default='0', max_length=1, verbose_name='نوع ملک'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='wc',
            field=models.CharField(choices=[('1', '1-2'), ('2', '3-4'), ('3', '5-6')], default='1', max_length=1, verbose_name='سرویس بهداشتی'),
        ),
    ]
