from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
from django.db import IntegrityError
from .models import Producto
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                auth_login(request, user)
                return redirect('login')
            except IntegrityError:
                return render(request, 'register.html', {"form": UserCreationForm, "error": "Usuario ya existe."})
        else:
            return render(request, 'register.html', {"form": UserCreationForm, "error": "Contraseña no coincide."})

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            # Verificar si el usuario existe en la base de datos
            if User.objects.filter(username=username).exists():
                # Usuario existe pero contraseña incorrecta
                return JsonResponse({'error': 'Contraseña incorrecta'})
            else:
                # Usuario no existe
                return JsonResponse({'error': 'Usuario no registrado'})
        else:
            auth_login(request, user)
            return redirect('product')
        
def product(request):
    return render(request, 'product.html', {"product": "Producto de ejemplo"})
        
@csrf_exempt
def agregar_producto(request):
    if request.method == 'POST':
        try:
            # Decodificamos los datos JSON del request
            data = json.loads(request.body)

            # Crear el producto con los datos recibidos
            producto = Producto.objects.create(
                codigo=data['codigo'],
                cantidad=data['cantidad'],
                descripcion=data['descripcion'],
                categoria=data['categoria'],
                precio_unitario=data['precio_unitario'],
                costo_unitario=data['costo_unitario']
            )

            # Guardar el producto en la base de datos
            producto.save()

            # Devolver una respuesta JSON exitosa
            return JsonResponse({'status': 'success', 'message': 'Producto guardado correctamente'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    # Si alguien intenta acceder a esta vista por GET, devolvemos una respuesta clara
    return JsonResponse({'status': 'error', 'message': 'Método GET no permitido'}, status=405)