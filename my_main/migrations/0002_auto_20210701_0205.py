# Generated by Django 3.1.5 on 2021-07-01 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ch_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
