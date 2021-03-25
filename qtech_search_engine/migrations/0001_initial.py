# Generated by Django 3.1.4 on 2021-03-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeywordDescriptionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('times_searched', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
