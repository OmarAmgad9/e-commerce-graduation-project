# Generated by Django 4.2.6 on 2023-11-01 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_remove_category_parent_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='update_time',
        ),
    ]
