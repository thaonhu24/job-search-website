# Generated by Django 3.2.7 on 2021-11-17 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comfirm',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 15, 59, 52, 795390)),
        ),
    ]
