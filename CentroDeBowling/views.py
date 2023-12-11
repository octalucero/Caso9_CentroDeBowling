from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.contrib  import messages


class BaseView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        logout(request)
        return redirect('index')


class LoginView(View):
    template_name = 'registration/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"Usuario {username} autenticado correctamente")
                return render(request, 'index.html')
            else:
                print(f"Usuario {username} {password}")
                print(user)
                return render(request, self.template_name, {'error_message': 'Credenciales inválidas'})
        except Exception as e:
            print(f"Excepción durante la autenticación: {e}")
            return render(request, self.template_name, {'error_message': 'Error durante la autenticación'})


def reserva(request):
    if request.method == 'POST':
        fecha = request.POST['fecha']
        hora = request.POST['hora_inicio']
        reserva = Reserva(dia_reserva=fecha,hora_reserva=hora)
        reserva.save()
        return render(request,'reservar.html')
    return render(request,'reservar.html')


class ReservarView(View):
    template_name = 'reservar.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        # Verificar si el usuario está autenticado
        if request.user.is_authenticated:
            # Obtener los datos del formulario
            fecha = request.POST.get('fecha')
            hora = request.POST.get('hora_inicio')
            
            # Obtener el ID del usuario autenticado
            cliente_id = request.user.id
            
            # Crear la reserva con cliente_id
            reserva = Reserva.objects.create(
                dia_reserva=fecha,
                hora_reserva=hora,
                cliente_id=cliente_id
            )
            
            return HttpResponse("¡Reserva creada exitosamente!")
        else:
            messages.error(request, "Debe iniciar sesión para realizar una reserva.")
            return redirect('reservar')
def registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        usuario = request.POST['username']
        direccion = request.POST['direccion']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        dni = request.POST['dni']  
        clave = request.POST['password']
        
        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            usuario=usuario,
            direccion=direccion,
            correo=correo,
            num_telefono=telefono,
            dni=dni,  
            contraseña=clave
        )
        
        cliente.save()
        return render(request, 'registration/registro.html')
    
    return render(request, 'registration/registro.html')

class ReservasView(View):
    template_name = 'rev.html'

    def get(self, request):
        return render(request, self.template_name)
    
class EditView(View):
    template_name = 'edit.html'

    def get(self, request):
        # Obtener la reserva asociada al cliente actual
        usuario = request.user.id
        reserva = Reserva.objects.filter(cliente__id=usuario)

        if reserva:
            # Renderizar el formulario de edición con los datos de la reserva
            return render(request, self.template_name, {'reserva': reserva})
        else:
            messages.error(request, "No hay reserva para editar.")
            return redirect('reservar')

    def post(self, request):
        reserva = Reserva.objects.all()

    

class ReadView(View):
    template_name = 'read.html'

    def get(self, request):
        # Obtener la reserva asociada al cliente actual
        usuario = request.user.id
        reserva = Reserva.objects.filter(cliente__id=usuario)

        if reserva:
            # Renderizar el formulario de edición con los datos de la reserva
            return render(request, self.template_name, {'reserva': reserva})
        else:
            messages.error(request, "No hay reservas.")
            return redirect('reservar')

    def post(self, request):
         cliente_id = request.POST.get('cliente_id')
         dia_reserva = request.POST.get('dia_reserva')
         hora_reserva = request.POST.get('hora_reserva')

        # Buscar la reserva en base a la combinación de campos
         reserva = Reserva.objects.filter(cliente_id=cliente_id, dia_reserva=dia_reserva, hora_reserva=hora_reserva).first()

         if reserva:
            # Actualizar los campos de la reserva directamente
            reserva.cliente_id = request.POST.get('cliente_id')
            reserva.dia_reserva = request.POST.get('dia_reserva')
            reserva.hora_reserva = request.POST.get('hora_reserva')
            # Agregar más campos según sea necesario

            reserva.save()

            messages.success(request, "Reserva actualizada exitosamente.")
            return redirect('reservas')
         else:
            messages.error(request, "No se encontró la reserva para editar.")
            return redirect('reservar')
    
class DeleteView(View):
    template_name = 'borrar.html'

    def get(self, request):
        # Obtener la reserva asociada al cliente actual
        usuario = request.user.id
        reserva = Reserva.objects.filter(cliente__id=usuario)

        if reserva:
            # Renderizar el formulario de edición con los datos de la reserva
            return render(request, self.template_name, {'reserva': reserva})
        else:
            messages.error(request, "No hay reservas.")
            return redirect('reservar')

    def post(self, request):
        reserva = Reserva.objects.all()
    

class ClienteView(View):
    template_name = 'registration/registro.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):  # Agrega el parámetro self aquí
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        usuario = request.POST['username']
        direccion = request.POST['direccion']

        correo = request.POST['correo']
        telefono = request.POST['telefono']
        dni = request.POST['dni']  
        clave = request.POST['password']
        hashed_password = make_password(clave)

        cliente = Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            username=usuario,
            direccion=direccion,
            correo=correo,
            num_telefono=telefono,
            dni=dni,  
            password=hashed_password
        )


        return redirect(request, 'index.html')
    

class CafeteriaView(View):
    template_name = "cafeteria.html"
    productos = Producto.objects.all()

    def get(self, request):
        return render(request, self.template_name, {'productos': self.productos})

    def post(self, request):
        productos_nombres = request.POST.getlist('productos')
        cliente_id = request.user.id  # Obtén el ID del cliente desde la sesión o según tu lógica

        for producto_nombre in productos_nombres:
            # Obtén el objeto Producto por nombre
            producto = Producto.objects.get(nombre=producto_nombre)

            # Crea una entrada en ProductoCliente para el cliente y el producto seleccionado
            ProductoCliente.objects.create(producto=producto, cliente_id=cliente_id)

        return HttpResponse("¡Productos agregados exitosamente!")