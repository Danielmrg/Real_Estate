# Generated by Django 3.0 on 2021-03-24 09:59

import advert.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0005_auto_20210214_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='is_privet',
        ),
        migrations.AddField(
            model_name='advert',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='ادرس'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='category',
            field=models.CharField(choices=[('0', 'همه نوع قرار داد'), ('2', 'فروش'), ('3', 'رهن'), ('4', 'اجاره')], default='0', max_length=1, verbose_name='وضعیت اگهی'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='house_type',
            field=models.CharField(choices=[('0', 'همه نوع'), ('1', 'ویلایی'), ('2', 'آپارتمانی'), ('3', 'زمین'), ('4', 'سایر موارد')], default='0', max_length=1, verbose_name='وضعیت اگهی'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='poster',
            field=models.ImageField(default='image_default\\default.jpg', upload_to=advert.models.change_file_name, verbose_name='پستر'),
        ),
    ]
