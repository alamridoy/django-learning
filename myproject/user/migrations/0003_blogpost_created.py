# Generated by Django 3.2.7 on 2022-06-21 05:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
