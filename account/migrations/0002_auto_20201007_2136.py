# Generated by Django 3.1.1 on 2020-10-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='profile_pic.jpg', upload_to='users/%Y/%m/%d/'),
        ),
    ]