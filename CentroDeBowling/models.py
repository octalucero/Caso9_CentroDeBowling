from django.db import models

# Create your models here.

class Client(models.Model):
    num_unico = models.IntegerField()
    nombre = models.CharField(max_length=25)
    direccion = models.CharField(max_length=75)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=75)

    def hacer_reserva(self):
        pass



class Reserva(models.Model):
    dia_reserva = models.DateField()
    hora_reserva = models.TimeField()

    def calcular_costo_total(self):
        pass

    def cobrar_costo_total(self):
        pass

class Cafeteria(models.Model):
    nombre = models.CharField()
    descripcion = models.CharField()
    precio = models.IntegerField()

class Pedido(models.Model):
    descripicion = models.CharField()
    