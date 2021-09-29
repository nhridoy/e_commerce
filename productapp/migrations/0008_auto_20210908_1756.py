# Generated by Django 3.2.6 on 2021-09-08 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productapp', '0007_auto_20210908_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avg_rating',
            field=models.IntegerField(blank=True, help_text='Do not Edit!', null=True, verbose_name='Average Rating'),
        ),
        migrations.AddField(
            model_name='product',
            name='total_rating',
            field=models.IntegerField(blank=True, help_text='Do not Edit!', null=True, verbose_name='Total Rating'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_rating', models.IntegerField(verbose_name='Rating')),
                ('product_comment', models.TextField(verbose_name='Comment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_ratings', to='productapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
