from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Pista)
admin.site.register(EstadoPista)
admin.site.register(HistorialEstadoPista)
admin.site.register(Reserva)
admin.site.register(EstadoReserva)
admin.site.register(HistorialEstadoReserva)
admin.site.register(Menu)
admin.site.register(ProductoMenu)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(PrecioProducto)
admin.site.register(AsignacionPedido)
admin.site.register(Partida)
admin.site.register(Fila)
admin.site.register(Turno)
admin.site.register(ProductoCliente)
