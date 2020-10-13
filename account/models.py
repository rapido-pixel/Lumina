from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    photo = models.ImageField(default='profile_pic.jpg', upload_to='users/%Y/%m/%d/')
    about = models.TextField(max_length=200, null=True, blank=True)
    link = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
