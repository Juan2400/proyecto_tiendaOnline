from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, PerfilCliente

class ClienteRegistroForm(UserCreationForm):
    nombres = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese nombres', 'id': 'names'})
    )
    apellido_paterno = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese apellido paterno', 'id': 'apellido_paterno'})
    )
    apellido_materno = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese apellido materno', 'id': 'apellido_materno'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Ingrese correo electrónico', 'id': 'email'})
    )
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese número de celular', 'id': 'phone'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese contraseña', 'id': 'password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme contraseña', 'id': 'confirmPassword'})
    )

    class Meta:
        model = CustomUser
        fields = ['nombres', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico', 'id': 'email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'id': 'password'})
    )

#Crear el formulario para editar la dirección
class PerfilForm(forms.ModelForm):
    direccion = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Ingrese su dirección', 'id': 'direccion', 'rows': 3})
    )
    
    class Meta:
        model = PerfilCliente
        fields = ['direccion']