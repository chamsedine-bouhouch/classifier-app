# Generated by Django 4.0.4 on 2022-04-26 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0002_rename_caption_uploadimage_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='image_app.uploadimage')),
                ('result', models.CharField(max_length=20)),
            ],
        ),
    ]
