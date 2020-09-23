# Generated by Django 3.1.1 on 2020-09-23 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200923_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 23, 15, 28, 7, 377987)),
        ),
        migrations.AlterField(
            model_name='like',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 23, 15, 28, 7, 377305)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 23, 15, 28, 7, 376470), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_images'),
        ),
    ]
