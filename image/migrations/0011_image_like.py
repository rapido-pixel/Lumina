# Generated by Django 3.1.1 on 2020-10-10 20:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image', '0010_remove_image_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]