from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
from django.db import IntegrityError

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
                return redirect('product')
            except IntegrityError:
                return render(request, 'register.html', {"form": UserCreationForm, "error": "Usuario ya existe."})
        else:
            return render(request, 'register.html', {"form": UserCreationForm, "error": "Contraseña no coincide."})

def product(request):
    return render(request, 'product.html', {"product": "Producto de ejemplo"})

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': "Usuario y contraseña incorrectos"
            })
        else:
            auth_login(request, user)
            return redirect('product')

