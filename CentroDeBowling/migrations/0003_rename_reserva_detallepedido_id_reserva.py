# Generated by Django 4.2.4 on 2023-12-10 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CentroDeBowling', '0002_remove_reserva_id_reserva_id_reserva'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallepedido',
            old_name='reserva',
            new_name='id_reserva',
        ),
    ]
