# Generated by Django 5.0.4 on 2024-05-08 02:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_article_alter_comment_author'),
        ('user_management', '0004_alter_profile_display_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_articles', to='user_management.profile'),
        ),
        migrations.AlterField(
            model_name='article',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
    ]
