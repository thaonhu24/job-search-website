# Generated by Django 3.2.7 on 2021-11-03 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='field_job',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 2, 3, 7, 639034)),
        ),
    ]
