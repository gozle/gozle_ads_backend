# Generated by Django 4.2.5 on 2023-10-04 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='age_from',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='age_to',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='imput',
            name='age_from',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='imput',
            name='age_to',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='age_from',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='age_to',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]