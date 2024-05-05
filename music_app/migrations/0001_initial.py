# Generated by Django 5.0.4 on 2024-05-04 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('tahun_rilis', models.IntegerField()),
                ('artis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.artis')),
            ],
        ),
        migrations.CreateModel(
            name='Lagu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('durasi', models.DurationField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.album')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('lagu', models.ManyToManyField(to='music_app.lagu')),
            ],
        ),
    ]