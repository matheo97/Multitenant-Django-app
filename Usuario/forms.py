from .models import *
from django import forms
from django.contrib.auth.forms import * 
from django.forms import ModelForm
from captcha.fields import CaptchaField

class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email"), max_length=254)
    

class IniciarSesionForm(AuthenticationForm):

	class Meta:
		model = User

		username = forms.CharField(label="Correo", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))
		password = forms.CharField(label="Contrasena", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
		
         
class CrearAdministradorForm(UserCreationForm):
    class Meta:
        model = Administrador
        fields = (
            'primer_nombre',
            'primer_apellido',
            'segundo_apellido',
            'tipo_documento_identificacion',
            'numero_documento_identificacion',
            'fecha_nacimiento',            
            'correo_electronico',
            'telefono',
            'username',
            'password1',
            'password2',
         )

class CrearDigitadorForm(UserCreationForm):
    class Meta:
        model = Digitador
        fields = (
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apellido',
            'tipo_documento_identificacion',
            'numero_documento_identificacion',
            'fecha_nacimiento',            
            'correo_electronico',
            'telefono',
            'username',
            'password1',
            'password2',
         )

class ModificarUsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = (
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apellido',
            'tipo_documento_identificacion',
            'numero_documento_identificacion',
            'fecha_nacimiento',            
            'correo_electronico',
            'telefono',
            'username',
         )		

class CrearClienteForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = (
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apellido',
            'tipo_documento_identificacion',
            'numero_documento_identificacion',
            'fecha_nacimiento',            
            'correo_electronico',
            'telefono',
            'username',
            'password1',
            'password2',
            'tarjeta_credito',
         )


class ModificarClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = (
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apellido',
            'tipo_documento_identificacion',
            'numero_documento_identificacion',
            'fecha_nacimiento',            
            'correo_electronico',
            'telefono',
            'username',
            'tarjeta_credito',
         )		
         
