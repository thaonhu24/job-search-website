# Generated by Django 3.2.8 on 2021-11-27 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20211128_0114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_updated_iterested_job',
            new_name='is_updated_interested_job',
        ),
    ]
