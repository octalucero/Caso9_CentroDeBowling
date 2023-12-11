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


class Reserva(models.Model):
    dia_reserva = models.DateField()
    hora_reserva = models.TimeField()   
    cant_personas = models.IntegerField(null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.cliente.username} - {self.dia_reserva} - {self.hora_reserva}"

class Meta:
        # Definir una restricción única para garantizar la combinación única de cliente, fecha y hora
        unique_together = ['cliente', 'dia_reserva', 'hora_reserva']

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


class ProductoMenu(models.Model):
    precio = models.FloatField()
    productoMenu = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()

    def __str__(self):
        return self.nombre




class ProductoCliente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cliente.username}"

class Pedido(models.Model):
    descripcion = models.TextField()
    listapedidos = models.ManyToManyField('Pedido')
    hora = models.DateTimeField()


class DetallePedido(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    descripcion = models.TextField()



class PrecioProducto(models.Model):
    precio = models.FloatField()
    fecha_vigencia = models.DateField()
    pruducto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)


class AsignacionPedido(models.Model):
    descripcion = models.TextField()
    precio = models.IntegerField()



class Puntaje(models.Model):
    nombre = models.CharField(max_length=100)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    turno1 = models.IntegerField()
    turno2 = models.IntegerField()
    turno3 = models.IntegerField()
    turno4 = models.IntegerField()
    turno5 = models.IntegerField()
    total = models.IntegerField(null=True)