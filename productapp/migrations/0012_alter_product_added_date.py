# Generated by Django 3.2.6 on 2021-09-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0011_product_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
    ]
