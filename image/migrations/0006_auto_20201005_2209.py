# Generated by Django 3.1.1 on 2020-10-05 22:09

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):
    dependencies = [
        ('image', '0005_image_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='thumb',
            field=easy_thumbnails.fields.ThumbnailerImageField(default=None, null=True, upload_to=''),
        ),
    ]
