# Generated by Django 3.2.9 on 2021-11-22 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='yt_link',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]