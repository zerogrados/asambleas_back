# Generated by Django 3.0 on 2020-05-21 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respuestas', '0004_respuestadecimal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestadecimal',
            name='respuesta_decimal',
            field=models.DecimalField(decimal_places=3, max_digits=20),
        ),
    ]