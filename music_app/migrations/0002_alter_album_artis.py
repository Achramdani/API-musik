# Generated by Django 5.0.4 on 2024-05-05 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='music_app.artis'),
        ),
    ]
