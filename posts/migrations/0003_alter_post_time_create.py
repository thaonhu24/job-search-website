# Generated by Django 3.2.7 on 2021-11-09 04:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211109_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 11, 31, 15, 819634)),
        ),
    ]