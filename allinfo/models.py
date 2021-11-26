from django.db import models

# Create your models here.
class Allinfo(models.Model):

    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    fb_link = models.URLField(max_length=255)
    insta_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    yt_link = models.URLField(max_length=255)

    def __str__(self) -> str:
        return self.email
