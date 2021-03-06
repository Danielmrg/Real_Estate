# Generated by Django 3.0 on 2021-03-24 11:13

import advert.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0008_auto_20210324_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='baths',
            field=models.CharField(choices=[('0', 'هر تعداد'), ('1', '1-2'), ('2', '3-4'), ('3', '5-6')], default='1', max_length=1, verbose_name='حمام'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='beds',
            field=models.CharField(choices=[('0', 'هر تعداد'), ('1', '1-2'), ('2', '3-4'), ('3', '5-6')], default='1', max_length=1, verbose_name='اتاق خواب'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='poster',
            field=models.ImageField(default='image_default\\default.jpg', upload_to=advert.models.change_file_name, verbose_name='پستر'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='wc',
            field=models.CharField(choices=[('0', 'هر تعداد'), ('1', '1-2'), ('2', '3-4'), ('3', '5-6')], default='1', max_length=1, verbose_name='سرویس بهداشتی'),
        ),
    ]
