# Generated by Django 3.2.8 on 2021-11-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='summary',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
