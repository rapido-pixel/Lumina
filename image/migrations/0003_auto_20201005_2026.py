# Generated by Django 3.1.1 on 2020-10-05 20:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('image', '0002_auto_20200927_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='created_by',
            new_name='created',
        ),
    ]
