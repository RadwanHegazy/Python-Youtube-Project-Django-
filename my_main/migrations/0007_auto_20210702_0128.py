# Generated by Django 3.1.5 on 2021-07-01 23:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_main', '0006_auto_20210701_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='bg',
            field=models.ImageField(default='static/fg-images/def/def_bg.jpg', upload_to='static/fg-images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fg',
            field=models.ImageField(default='static/fg-images/def/def_user.png', upload_to='static/fg-images/'),
        ),
    ]
