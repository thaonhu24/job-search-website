# Generated by Django 3.2.8 on 2021-11-30 03:34

import ckeditor.fields
import datetime
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fields_job', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_skill', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=64, null=True), blank=True, null=True, size=10)),
                ('name_post', models.CharField(max_length=200)),
                ('time_create', models.DateTimeField(default=datetime.datetime(2021, 11, 30, 10, 34, 8, 440826))),
                ('experience_required', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('content_post', ckeditor.fields.RichTextField(max_length=2000)),
                ('type_job', models.CharField(max_length=100)),
                ('confirm', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('field_job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fields_job.fieldjob')),
            ],
        ),
    ]
