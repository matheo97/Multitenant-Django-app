from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Usuario(User):

	IDENTIFICACION_CHOICES = (('CC','Cedula de ciudadania'),('TI','Tarjeta de identidad'),('CE','Cedula de extranjeria'))

	ESTADO_CHOICES = (('ACTIVO','Activo'),('INACTIVO','Inactivo'))
	fecha_nacimiento = models.DateField(verbose_name="fecha de nacimiento")
	tipo_documento_identificacion = models.CharField(max_length=30,verbose_name="tipo de identificacion",choices = IDENTIFICACION_CHOICES)
	numero_documento_identificacion = models.CharField(max_length=30,verbose_name="numero de documento de identificacion")	
	correo_electronico = models.EmailField(max_length=100,verbose_name="correo electronico")
	telefono = models.CharField(max_length=20,verbose_name="numero telefonico")
	estado = models.CharField(max_length=20,verbose_name="estado",default = 'ACTIVO',choices = ESTADO_CHOICES)
	primer_nombre = models.CharField(max_length=100,verbose_name="primer nombre")
	segundo_nombre = models.CharField(max_length=100,verbose_name="segundo nombre", null=True, default="")
	primer_apellido = models.CharField(max_length=100,verbose_name="primer apellido")
	segundo_apellido = models.CharField(max_length=100,verbose_name="segundo apellido")
	
	is_admin = models.BooleanField(default=False)
	is_cliente = models.BooleanField(default=False)
	is_digitador = models.BooleanField(default=False)

	def __str__(self):	
		return '%s %s %s %s' % (self.primer_nombre , self.segundo_nombre , self.primer_apellido , self.segundo_apellido)
		
	def nombre(self):	
		return '%s %s %s %s' % (self.primer_nombre , self.segundo_nombre , self.primer_apellido , self.segundo_apellido)


class Administrador(Usuario):
	
	class Meta:
		db_table = 'usuario_administrador'
		
	def tipo(self):	
		return '%s' % ("Administrador")
		
		
class Digitador(Usuario):
	
	class Meta:
		db_table = 'usuario_digitador'
		
	def tipo(self):	
		return '%s' % ("Digitador")


class Cliente(Usuario):

	tarjeta_credito = models.CharField(max_length=200,verbose_name="numero de tarjeta de credito")
	fecha_registro = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		db_table = 'usuario_cliente'
		
	def tipo(self):	
		return '%s' % ("Cliente")