# Generated by Django 3.0 on 2021-02-14 17:07

import advert.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0004_auto_20210214_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='poster',
            field=models.ImageField(default='image_default\\default.jpg', upload_to=advert.models.change_file_name, verbose_name='پستر'),
        ),
    ]
