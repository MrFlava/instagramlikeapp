# Generated by Django 3.1.1 on 2020-09-22 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 22, 8, 49, 28, 241802), verbose_name='date published'),
        ),
    ]