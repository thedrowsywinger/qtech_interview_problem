# Generated by Django 3.1.4 on 2021-03-25 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qtech_search_engine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyworddescriptionmodel',
            name='user',
            field=models.ManyToManyField(to='qtech_search_engine.AllUsers'),
        ),
    ]
