# Generated by Django 3.2.9 on 2022-03-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0015_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(blank=True, max_length=256, unique=True),
        ),
    ]
