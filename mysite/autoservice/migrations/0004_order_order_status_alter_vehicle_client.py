# Generated by Django 5.0.1 on 2024-01-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0003_alter_model_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(blank=True, choices=[('r', 'Received'), ('c', 'Confirmed'), ('ip', 'In-progress'), ('co', 'Complete')], default='r', help_text='Order status', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='client',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Client'),
        ),
    ]
