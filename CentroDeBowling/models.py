from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("El campo de nombre de usuario es obligatorio")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("dni", 1)  # Añade esta línea

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusername debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusername debe tener is_superuser=True.")

        return self.create_user(username, password, **extra_fields)

class Pista(models.Model):
    numero_identificativo = models.CharField(max_length=50)
    max_capacidad = models.IntegerField()

    def crear(self):
        # Implementa la lógica para crear una pista
        pass

    def verificarEstadoPista(self):
        # Implementa la lógica para verificar el estado de la pista
        pass

class EstadoPista(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class HistorialEstadoPista(models.Model):
    fecha_hora_inicio = models.CharField(max_length=50)
    fecha_hora_fin = models.DateTimeField()
    estado = models.ForeignKey(EstadoPista, on_delete=models.CASCADE)

class Cliente(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    direccion = models.TextField()
    num_telefono = models.CharField(max_length=50)
    correo = models.EmailField()
    dni = models.IntegerField()
    contraseña = models.CharField(max_length=100)
    
    is_staff = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["correo"]

    objects = CustomUserManager()


    def crear(self):
        # Implementa la lógica para crear un cliente
        pass

    def hacerReserva(self):
        # Implementa la lógica para hacer una reserva
        pass

class Reserva(models.Model):
    dia_reserva = models.DateField()
    hora_reserva = models.TimeField()   
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def crear(self):
        pass
    def mostrar(self):
        # Implementa la lógica para mostrar la reserva
        pass

    def cancelar(self):
        # Implementa la lógica para cancelar la reserva
        pass

    def calcularCostoTotal(self):
        # Implementa la lógica para calcular el costo total de la reserva
        pass

    def cobrarCostoTotal(self):
        # Implementa la lógica para cobrar el costo total de la reserva
        pass

    def verificarEstadoReserva(self):
        # Implementa la lógica para verificar el estado de la reserva
        pass

class EstadoReserva(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class HistorialEstadoReserva(models.Model):
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    estado = models.ForeignKey(EstadoReserva, on_delete=models.CASCADE)

class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()

    def crear(self):
        # Implementa la lógica para crear un menú
        pass

    def mostrar(self):
        # Implementa la lógica para mostrar el menú
        pass

class ProductoMenu(models.Model):
    precio = models.FloatField()
    productoMenu = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

    def ActulizarPrecioProducto(self):
        pass


class ProductoCliente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cliente.username}"

class Pedido(models.Model):
    descripcion = models.TextField()
    listapedidos = models.ManyToManyField('Pedido')
    hora = models.DateTimeField()

    def crear(self):
        # Implementa la lógica para crear un pedido
        pass

    def cancelar(self):
        # Implementa la lógica para cancelar el pedido
        pass

    def registrarpedido(self):
        # Implementa la lógica para registrar el pedido
        pass

class DetallePedido(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def crear(self):
        pass

class PrecioProducto(models.Model):
    precio = models.FloatField()
    fecha_vigencia = models.DateField()
    pruducto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def verificarPrecioProducto(self):
        pass

class AsignacionPedido(models.Model):
    descripcion = models.TextField()
    precio = models.IntegerField()

    def verificaEleccionPedido(self):
        # Implementa la lógica para verificar la elección de un pedido
        pass

    def obetnerPrecio(self):
        # Implementa la lógica para obtener el precio de la asignación de pedido
        pass

class Partida(models.Model):
    identificador_unico = models.CharField(max_length=50)
    descripcion = models.TextField()

    def crear(self):
        # Implementa la lógica para crear una partida
        pass

    def cancelarPartida(self):
        # Implementa la lógica para cancelar una partida
        pass

    def calcularPuntajeTotal(self):
        # Implementa la lógica para calcular el puntaje total de la partida
        pass

    def calcularCantidadJugadores(self):
        # Implementa la lógica para calcular la cantidad de jugadores en la partida
        pass

class Fila(models.Model):
    identificador_unico = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    listaturnos = models.ManyToManyField('Turno')

    def crear(self):
        # Implementa la lógica para crear una fila
        pass

    def verificarListaTurnos(self):
        # Implementa la lógica para verificar la lista de turnos
        pass

class Turno(models.Model):
    descripcion = models.TextField()
    listatiradas = models.ManyToManyField('Tirada')

    def crear(self):
        # Implementa la lógica para crear un turno
        pass

    def Calcularpinostotales(self):
        # Implementa la lógica para calcular los pinos totales en un turno
        pass

    def verificarPosicion(self):
        # Implementa la lógica para verificar la posición en el turno
        pass

    def verificarListaTiradas(self):
        # Implementa la lógica para verificar la lista de tiradas en el turno
        pass

class DetalleTurno(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def calcularTurno(self):
        # Implementa la lógica para calcular un turno
        pass

class Tirada(models.Model):
    descripcion = models.TextField()
    pinos_derribados = models.IntegerField()

    def crear(self):
        # Implementa la lógica para registrar una tirada
        pass
