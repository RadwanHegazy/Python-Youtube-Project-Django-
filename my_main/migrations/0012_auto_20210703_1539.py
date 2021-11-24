# Generated by Django 3.1.5 on 2021-07-03 13:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_main', '0011_auto_20210703_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='dislikes',
            field=models.ManyToManyField(blank=True, null=True, related_name='VideoDislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='VideoLikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.ManyToManyField(blank=True, null=True, related_name='videoViews', to=settings.AUTH_USER_MODEL),
        ),
    ]
