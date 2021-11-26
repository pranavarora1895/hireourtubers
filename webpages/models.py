from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Team(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    yt_link = models.URLField(max_length=255, blank=True)
    fb_link = models.URLField(max_length=255)
    insta_link = models.URLField(max_length=255)
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d/")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name


class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    button_link = models.URLField(max_length=2000, blank=True)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.headline


class About(models.Model):
    
    headline1 = models.CharField(max_length=255)
    headline2 = models.CharField(max_length=255, blank=True)
    photo1 = models.ImageField(upload_to='media/about1/%Y/')
    photo2 = models.ImageField(upload_to='media/about2/%Y/')
    decription1 = RichTextField()
    decription2 = RichTextField()

    def __str__(self) -> str:
        return self.headline1

