from .models import *
from django import forms
from django.contrib.auth.forms import * 
from django.forms import ModelForm


class ModificarTenantForm(ModelForm):
    class Meta:
        model = Franquicia
        fields = (
            'nombre',
            'descripcion',
            'reportes_graficos',
            'color',
            'nav_var_color',
            'sidebar_grid',
            'tinte',
            'font' 
         )
         

class ModificarDominioForm(ModelForm):
    class Meta:
        model = Dominio
        fields = (
            'domain',
         )
         
         
class IniciarSesionForm(AuthenticationForm):

	class Meta:
		model = User

		username = forms.CharField(label="Usuario", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
		password = forms.CharField(label="Contrasena", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
		
		
		
class CrearAdministradorTenantsForm(UserCreationForm):
    class Meta:
        model = Administrador_tenants
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
        model = Administrador_tenants
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