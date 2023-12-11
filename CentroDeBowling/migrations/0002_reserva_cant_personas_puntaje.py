# Generated by Django 5.0 on 2023-12-11 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CentroDeBowling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='cant_personas',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Puntaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('turno1', models.IntegerField()),
                ('turno2', models.IntegerField()),
                ('turno3', models.IntegerField()),
                ('turno4', models.IntegerField()),
                ('turno5', models.IntegerField()),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CentroDeBowling.reserva')),
            ],
        ),
    ]
