# Generated by Django 3.0 on 2021-03-24 11:49

import advert.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0010_auto_20210324_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='poster',
            field=models.ImageField(default='image_default\\default.jpg', upload_to=advert.models.change_file_name, verbose_name='پستر'),
        ),
    ]