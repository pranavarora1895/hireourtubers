from django.db import models

# Create your models here.

class Contacttuber(models.Model):

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

class Contactinfo(models.Model):
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email