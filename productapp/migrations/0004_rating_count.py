# Generated by Django 3.2.6 on 2021-09-08 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_auto_20210908_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
