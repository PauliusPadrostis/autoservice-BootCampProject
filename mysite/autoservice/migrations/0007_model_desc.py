# Generated by Django 5.0.1 on 2024-01-17 12:34

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0006_order_client_order_return_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='desc',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
