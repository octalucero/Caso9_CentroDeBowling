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
        return render(request, self.template_name)
    
    def get(self, request, pk):
        reserva = get_object_or_404(Reserva, pk=pk)
        form = ReservarView(instance=reserva)
        return render(request, self.template_name, {'form': form, 'reserva': reserva})

    def post(self, request, pk):
        reserva = get_object_or_404(Reserva, pk=pk)
        form = ReservarView(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return HttpResponse("¡Reserva editada exitosamente!")
        return render(request, self.template_name, {'form': form, 'reserva': reserva})
    

class ReadView(View):
    template_name = 'read.html'

    def get(self, request):
        return render(request, self.template_name)
    
class DeleteView(View):
    template_name = 'borrar.html'

    def get(self, request):
        return render(request, self.template_name)
    

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