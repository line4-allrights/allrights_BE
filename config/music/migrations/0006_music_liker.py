# Generated by Django 4.2.7 on 2023-11-08 03:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0005_music_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='liker',
            field=models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]