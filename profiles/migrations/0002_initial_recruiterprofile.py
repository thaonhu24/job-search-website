# Generated by Django 3.2.8 on 2021-11-20 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    
    initial = True 

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruiterProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_updated_basic_information_company', models.BooleanField(default=False)),
                ('name_of_company', models.CharField(blank=True, max_length=128, null=True)),
                ('profile_picture_company', models.ImageField(blank=True, default='default-profile-picture.jpg', upload_to='profile-picture')),
                ('location_of_company', models.TextField(blank=True, max_length=256, null=True)),
                ('email_of_company', models.EmailField(blank=True, max_length=254, null=True)),
                ('hotline_of_company', models.TextField(blank=True, max_length=20, null=True)),
                ('website_of_company', models.TextField(blank=True, max_length=256, null=True)),
                ('business_field_of_company', models.TextField(blank=True, max_length=128, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_recruiter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Recruiter\'sProfile',
                'verbose_name_plural': 'Recruiter\'s Profiles',
            }
        ),
    ]
