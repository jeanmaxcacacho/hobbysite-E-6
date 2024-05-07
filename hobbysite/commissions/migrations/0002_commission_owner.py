# Generated by Django 5.0.2 on 2024-05-05 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile'),
            preserve_default=False,
        ),
    ]