# Generated by Django 4.2.6 on 2023-11-01 00:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_remove_product_created_at_remove_product_update_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]