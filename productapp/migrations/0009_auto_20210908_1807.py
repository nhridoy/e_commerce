# Generated by Django 3.2.6 on 2021-09-08 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0008_auto_20210908_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='avg_rating',
        ),
        migrations.RemoveField(
            model_name='product',
            name='total_rating',
        ),
    ]
