# Generated by Django 4.2.6 on 2023-10-30 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_category_id', models.IntegerField()),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, max_length=4000, null=True)),
                ('product_image', models.ImageField(upload_to='image/product')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.category')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.category')),
            ],
        ),
        migrations.CreateModel(
            name='VariationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=150)),
                ('variation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.variation')),
            ],
        ),
        migrations.CreateModel(
            name='product_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=20, null=True)),
                ('quantity_in_stock', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='image/product_items')),
                ('price', models.FloatField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.product')),
            ],
        ),
    ]
