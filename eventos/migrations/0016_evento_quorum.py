# Generated by Django 3.0 on 2020-05-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0015_auto_20200528_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='quorum',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=25),
        ),
    ]
