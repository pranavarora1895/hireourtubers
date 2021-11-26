from django.db import models
from datetime import datetime
# Create your models here.

class Hiretuber(models.Model):
    first_name  = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    tuber_id  = models.IntegerField()
    tuber_name = models.CharField(max_length=255)
    email  = models.EmailField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    phone = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self) -> str:
        return self.email