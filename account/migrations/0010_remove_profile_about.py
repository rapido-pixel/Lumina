# Generated by Django 3.1.1 on 2020-10-08 18:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0009_auto_20201008_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about',
        ),
    ]
