# Generated by Django 4.2.4 on 2023-12-11 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleTurno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EstadoPista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EstadoReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador_unico', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_identificativo', models.CharField(max_length=50)),
                ('max_capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductoMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('productoMenu', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tirada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('pinos_derribados', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('direccion', models.TextField()),
                ('num_telefono', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('dni', models.IntegerField()),
                ('contraseña', models.CharField(max_length=100)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('listatiradas', models.ManyToManyField(to='CentroDeBowling.tirada')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_reserva', models.DateField()),
                ('hora_reserva', models.TimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CentroDeBowling.producto')),
            ],
        ),
        migrations.CreateModel(
            name='PrecioProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('fecha_vigencia', models.DateField()),
                ('pruducto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CentroDeBowling.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('hora', models.DateTimeField()),
                ('listapedidos', models.ManyToManyField(to='CentroDeBowling.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialEstadoReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora_inicio', models.DateTimeField()),
                ('fecha_hora_fin', models.DateTimeField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CentroDeBowling.estadoreserva')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialEstadoPista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora_inicio', models.CharField(max_length=50)),
                ('fecha_hora_fin', models.DateTimeField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CentroDeBowling.estadopista')),
            ],
        ),
        migrations.CreateModel(
            name='Fila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador_unico', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('listaturnos', models.ManyToManyField(to='CentroDeBowling.turno')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CentroDeBowling.pedido')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CentroDeBowling.reserva')),
            ],
        ),
    ]
