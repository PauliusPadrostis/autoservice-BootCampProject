# Generated by Django 5.0.1 on 2024-01-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0004_order_order_status_alter_vehicle_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers', verbose_name='Cover'),
        ),
    ]