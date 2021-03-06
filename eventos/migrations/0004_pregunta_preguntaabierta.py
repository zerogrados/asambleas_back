# Generated by Django 3.0 on 2020-05-16 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20200516_0506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=500)),
                ('activa', models.BooleanField(default=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='PreguntaAbierta',
            fields=[
                ('pregunta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Pregunta')),
            ],
            bases=('eventos.pregunta',),
        ),
    ]
