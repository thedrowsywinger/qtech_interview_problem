# Generated by Django 3.1.4 on 2021-03-25 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qtech_search_engine', '0002_keyworddescriptionmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyworddescriptionmodel',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]