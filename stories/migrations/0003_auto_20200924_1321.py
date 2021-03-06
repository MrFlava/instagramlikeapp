# Generated by Django 3.1.1 on 2020-09-24 13:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0002_auto_20200924_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 24, 13, 21, 58, 384192), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='watchedstory',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchedstories', to='stories.story'),
        ),
        migrations.AlterField(
            model_name='watchedstory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchedstories', to=settings.AUTH_USER_MODEL),
        ),
    ]
