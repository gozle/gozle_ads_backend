# Generated by Django 4.2.5 on 2023-11-18 16:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_banner_devices_alter_imput_devices_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='imput',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]