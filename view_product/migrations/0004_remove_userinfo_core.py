# Generated by Django 5.0 on 2023-12-21 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_product', '0003_userinfo_ip_address_userinfo_referrer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='core',
        ),
    ]