# Generated by Django 2.2.15 on 2021-01-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitewebapp', '0019_auto_20210130_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditionanswers',
            name='ans',
            field=models.CharField(max_length=800),
        ),
    ]