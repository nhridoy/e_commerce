# Generated by Django 3.2.6 on 2021-09-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0009_auto_20210908_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(blank=True, max_length=256),
        ),
    ]
