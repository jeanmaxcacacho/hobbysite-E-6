# Generated by Django 5.0.4 on 2024-05-04 18:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Available', 'Available'), ('On sale', 'On sale'), ('Out of stock', 'Out of stock')], max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('product_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='merchstore.producttype')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('On cart', 'On cart'), ('To pay', 'To pay'), ('To ship', 'To ship'), ('To receive', 'To receive'), ('Delivered', 'Delivered')], max_length=20)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_management.profile')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchstore.product')),
            ],
        ),
    ]
