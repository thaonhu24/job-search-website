# Generated by Django 3.2.8 on 2021-11-30 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_profile_list_skil_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='list_skil_tag',
            new_name='list_skill_tag',
        ),
    ]
