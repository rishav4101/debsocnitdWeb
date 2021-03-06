# Generated by Django 2.2.15 on 2021-02-07 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitewebapp', '0021_auto_20210201_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='url1',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='event',
            name='url2',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='event',
            name='url3',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True, max_length=50000),
        ),
    ]
