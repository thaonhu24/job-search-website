# Generated by Django 3.2.7 on 2021-11-02 07:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fields_job', '__first__'),
        ('posts', '0005_auto_20211102_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='field_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fields_job.fieldjob'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 14, 2, 25, 787173)),
        ),
    ]
