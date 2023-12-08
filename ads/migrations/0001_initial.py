# Generated by Django 4.2.5 on 2023-11-26 06:56

import uuid

import django.core.validators
import multiselectfield.db.fields
from django.db import migrations, models

import ads.fields
import ads.models
import helpers.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('platforms', multiselectfield.db.fields.MultiSelectField(choices=[('app', 'App'), ('web', 'Web')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('min_age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(80)])),
                ('max_age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(80)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('starts_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('hidden', 'Hidden'), ('deleted', 'Deleted'), ('test', 'Test')], default='hidden', max_length=30)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('score', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', ads.fields.WEBPField(upload_to=ads.models.video_folder, verbose_name='Image')),
                ('video', models.FileField(upload_to='video/videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'm3u8'])])),
                ('skip_duration', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(20)])),
                ('cities', models.ManyToManyField(to='locations.city')),
                ('devices', models.ManyToManyField(to='ads.device')),
                ('provinces', models.ManyToManyField(to='locations.province')),
            ],
            options={
                'verbose_name': 'video',
            },
            bases=(helpers.mixins.TaskCreatorMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Imput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('min_age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(80)])),
                ('max_age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(80)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('starts_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('hidden', 'Hidden'), ('deleted', 'Deleted'), ('test', 'Test')], default='hidden', max_length=30)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('score', models.IntegerField(default=0)),
                ('image', ads.fields.WEBPField(upload_to=ads.models.imput_folder, verbose_name='Image')),
                ('cities', models.ManyToManyField(to='locations.city')),
                ('devices', models.ManyToManyField(to='ads.device')),
                ('provinces', models.ManyToManyField(to='locations.province')),
            ],
            options={
                'verbose_name': 'imput',
            },
            bases=(helpers.mixins.TaskCreatorMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('min_age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(80)])),
                ('max_age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(80)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('starts_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('hidden', 'Hidden'), ('deleted', 'Deleted'), ('test', 'Test')], default='hidden', max_length=30)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('score', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', ads.fields.WEBPField(upload_to=ads.models.banner_folder, verbose_name='Image')),
                ('cycle_duration', models.PositiveIntegerField(default=180, validators=[django.core.validators.MinValueValidator(60)])),
                ('cities', models.ManyToManyField(to='locations.city')),
                ('devices', models.ManyToManyField(to='ads.device')),
                ('provinces', models.ManyToManyField(to='locations.province')),
            ],
            options={
                'verbose_name': 'banner',
            },
            bases=(helpers.mixins.TaskCreatorMixin, models.Model),
        ),
    ]
