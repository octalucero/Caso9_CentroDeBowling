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
                return redirect('index')
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


class Iniciar1(View):
    template_name = 'iniciar1.html'

    def get(self, request, reserva_id):
        return render(request, self.template_name)
    
    def post(self, request, reserva_id):
        cant_personas = request.POST.get('cantidad_personas')
        
        reserva = Reserva.objects.get(id=reserva_id)
        reserva.cant_personas = cant_personas
        reserva.save()
        
        return redirect('iniciar2', reserva_id=reserva_id)


class Iniciar2(View):
    template_name = 'iniciar2.html'

    def get(self, request, reserva_id):
        reserva = Reserva.objects.get(id=reserva_id)
        context = {
            'reserva': reserva,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, reserva_id):
        # Obtén la reserva correspondiente al ID
        reserva = Reserva.objects.get(id=reserva_id)
        puntaje_num = []
        for jugador in range(1, reserva.cant_personas + 1):
            # Crea un objeto Puntaje para cada jugador y turno
            puntaje = Puntaje(
                nombre=f"Jugador {jugador}", 
                reserva=reserva,
            )

            # Inicializa el total para el jugador actual
            total_jugador = 0

            # Itera sobre los turnos y asigna los valores dinámicamente
            for turno in range(1, 6):
                campo_name = f"jugador_{jugador}_campo_{turno}"
                valor = request.POST.get(campo_name)
                setattr(puntaje, f"turno{turno}", valor)

                # Suma el valor al total del jugador
                total_jugador += int(valor) if valor else 0

            # Asigna el total al atributo 'total' del objeto Puntaje
            puntaje.total = total_jugador

            puntaje.save()  # Guarda el objeto Puntaje en la base de datos
            print(f"Datos del Puntaje (Jugador {jugador}): {puntaje.__dict__}")
            puntaje_num.append(puntaje.total)

        context = {
            'reserva': reserva,
            'puntajes': puntaje_num
        }
        return render(request, self.template_name, context)


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
            
            messages.success(request,"¡Reserva creada exitosamente!")
            return redirect('index')
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


class EditarView(View):
    template_name = 'editar.html'

    def get(self, request, reserva_id):
        return render(request, self.template_name)

    def post(self, request, reserva_id):
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora_inicio')
        
        try:
            reserva = Reserva.objects.get(id=reserva_id)

            reserva.dia_reserva=fecha
            reserva.hora_reserva=hora
            reserva.save()
            
            return HttpResponse("¡Reserva actualizada exitosamente!")
        except:
            return HttpResponse("¡Hubo un error!")

    


class ReadView(View):
    template_name = 'read.html'

    def get(self, request):
        # Obtener la reserva asociada al cliente actual
        usuario = request.user.id
        reserva = Reserva.objects.filter(cliente__id=usuario)

        return render(request, self.template_name, {'reserva': reserva})

    
class DeleteView(View):
    template_name = 'borrar.html'

    def get(self, request):
        # Obtener la reserva asociada al cliente actual
        usuario = request.user.id
        reserva = Reserva.objects.filter(cliente__id=usuario)

        return render(request, self.template_name, {'reserva': reserva})

    def post(self, request):
        reservaid = request.POST.get('id')

        reserva = Reserva.objects.get(id=reservaid)

        reserva.delete()
        usuario = request.user.id
        reservas = Reserva.objects.filter(cliente__id=usuario)

        return render(request, self.template_name, {'reserva': reservas})

    

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


        return redirect('index')
    

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