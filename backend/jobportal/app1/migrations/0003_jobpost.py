# Generated by Django 5.0.6 on 2024-05-23 13:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_user_city_user_image_user_pincode_user_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_location', models.CharField(max_length=225)),
                ('job_package', models.IntegerField()),
                ('job_logo', models.ImageField(null=True, upload_to='jobpost_image')),
                ('qualification', models.CharField(max_length=225)),
                ('experience', models.CharField(choices=[('experience', 'experienced'), ('fresher', 'fresher')], max_length=225, null=True)),
                ('job_description', models.CharField(max_length=225)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
