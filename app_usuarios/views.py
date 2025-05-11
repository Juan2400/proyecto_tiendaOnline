from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import ClienteRegistroForm, CustomAuthenticationForm, PerfilForm
from .models import PerfilCliente

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Asignar al grupo de clientes
            try:
                grupo_cliente = Group.objects.get(name='cliente')
                user.groups.add(grupo_cliente)
            except Group.DoesNotExist:
                # Crear el grupo si no existe
                grupo_cliente = Group.objects.create(name='cliente')
                user.groups.add(grupo_cliente)
            
            # Autenticar y hacer login
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "¡Registro exitoso!")
                return redirect('Home')  # Redirigir a la página principal
    else:
        form = ClienteRegistroForm()
    
    return render(request, 'app_usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "¡Has iniciado sesión correctamente!")
                return redirect('Home')  # Redirigir a la página principal
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'app_usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('Home')

@login_required
def perfil(request):
    # Mostrar el perfil del usuario
    try:
        perfil_cliente = request.user.perfilcliente
    except PerfilCliente.DoesNotExist:
        # Crear perfil si no existe
        perfil_cliente = PerfilCliente.objects.create(usuario=request.user)
    
    return render(request, 'app_usuarios/perfil.html', {'perfil': perfil_cliente})

@login_required
def editar_perfil(request):
    try:
        perfil_cliente = request.user.perfilcliente
    except PerfilCliente.DoesNotExist:
        perfil_cliente = PerfilCliente.objects.create(usuario=request.user)
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil_cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Perfil actualizado correctamente!")
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil_cliente)
    
    return render(request, 'app_usuarios/editar_perfil.html', {'form': form})