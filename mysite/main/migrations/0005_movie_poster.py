# Generated by Django 2.2.13 on 2020-08-27 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200826_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.CharField(default='ddddd', max_length=150),
            preserve_default=False,
        ),
    ]
