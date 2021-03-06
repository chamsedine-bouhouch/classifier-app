# Generated by Django 4.0.4 on 2022-04-26 10:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0003_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
