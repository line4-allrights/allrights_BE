# Generated by Django 4.2.7 on 2023-11-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_alter_music_length_alter_music_liker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='length',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]