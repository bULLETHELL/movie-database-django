# Generated by Django 2.2.13 on 2020-08-26 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='production_year',
        ),
    ]
