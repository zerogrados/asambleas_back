# Generated by Django 3.0 on 2020-06-04 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0025_auto_20200602_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='asambleista',
            name='cantidadPoderes',
            field=models.IntegerField(default=0),
        ),
    ]
