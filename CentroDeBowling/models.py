from django.db import models

# Create your models here.

class Client(models.Model):
    num_unico = models.IntegerField()
    nombre = models.CharField(max_length=25)
    direccion = models.CharField(max_length=75)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=75)