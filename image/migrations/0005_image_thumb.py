# Generated by Django 3.1.1 on 2020-10-05 22:07

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):
    dependencies = [
        ('image', '0004_auto_20201005_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumb',
            field=easy_thumbnails.fields.ThumbnailerImageField(default=None, upload_to=''),
        ),
    ]
