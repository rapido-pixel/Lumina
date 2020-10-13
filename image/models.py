from django.db import models
from django.conf import settings


class Image(models.Model):
    created = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='created')
    title = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/1')

    def __str__(self):
        return self.title
