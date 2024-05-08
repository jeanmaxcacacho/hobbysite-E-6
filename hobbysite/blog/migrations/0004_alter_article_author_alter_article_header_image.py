# Generated by Django 5.0.4 on 2024-05-06 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_author_article_header_image_comment'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to='user_management.profile'),
        ),
        migrations.AlterField(
            model_name='article',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/'),
        ),
    ]