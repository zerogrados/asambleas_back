# Generated by Django 3.0 on 2020-06-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0023_auto_20200601_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='asambleista',
            name='correo_enviado',
            field=models.BooleanField(default=False),
        ),
    ]
