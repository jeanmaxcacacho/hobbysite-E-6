# Generated by Django 5.0.4 on 2024-05-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_profile_display_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='display_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/user_management/display_picture'),
        ),
    ]
