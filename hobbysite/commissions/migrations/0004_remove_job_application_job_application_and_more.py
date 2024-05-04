# Generated by Django 5.0.2 on 2024-05-04 13:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0003_commission_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_application',
            name='job_application',
        ),
        migrations.AddField(
            model_name='job_application',
            name='Job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Job', to='commissions.job'),
            preserve_default=False,
        ),
    ]
