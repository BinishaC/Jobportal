# Generated by Django 5.0.6 on 2024-05-25 04:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_savedjobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='liked_by',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
