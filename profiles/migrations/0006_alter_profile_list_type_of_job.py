# Generated by Django 3.2.8 on 2021-11-29 08:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_rename_is_updated_iterested_job_profile_is_updated_interested_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='list_type_of_job',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=16, null=True), null=True, size=4),
        ),
    ]