# Generated by Django 5.0.1 on 2024-01-15 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='autoservice.service'),
            preserve_default=False,
        ),
    ]