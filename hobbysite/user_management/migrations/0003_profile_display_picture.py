# Generated by Django 5.0.4 on 2024-05-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_profile_display_name_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='display_picture',
            field=models.ImageField(blank=True, null=True, upload_to='user_management/display_picture'),
        ),
    ]