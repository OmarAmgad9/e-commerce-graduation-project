# Generated by Django 4.2.6 on 2023-11-01 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_customuser_last_login_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
