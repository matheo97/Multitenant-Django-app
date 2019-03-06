from __future__ import unicode_literals

from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import User

class Franquicia(TenantMixin):
    
    ESTADO_CHOICES = (('ACTIVO','Activo'),('INACTIVO','Inactivo'))
    
    #Opciones para los modulos
    COLORES_CHOICES = (('red','Rojo'),('purple','Morado'),('orange','Naranja'),('default','Default'),('blue','Azul'),('black','Negro'))
    NAVCOLORES_CHOICES = (('navbar-inverse','inverse'),('navbar-default','default'))
    SIDEBAR_CHOICES = (('a','No'),('sidebar-grid','Si'))
    TINTE_CHOICES = (('a','No'),('flat-black','Si'))
    FONT_CHOICES = (('a','Defecto'),('font-family: ' + 'Mogra' + ', cursive;','Mogra'), ('font-family: ' + 'Josefin Sans' + ', sans-serif;','Josefin Sans'),
    ('font-family: ' + 'Pacifico' + ', cursive;','Pacifico'), ('font-family: ' + 'Shadows Into Light' + ', cursive;','Shadows Into Light'),
    ('font-family: ' + 'Gudea' + ', sans-serif;','Gudea'))
    
    
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=20,verbose_name="estado",default = 'ACTIVO',choices = ESTADO_CHOICES)
    reportes_graficos = models.CharField(max_length=20,verbose_name="reportes graficos",default = 'ACTIVO',choices = ESTADO_CHOICES)
    color = models.CharField(max_length=20,verbose_name="color tema", default = 'default',choices = COLORES_CHOICES)
    nav_var_color = models.CharField(max_length=20,verbose_name="color nav-var", default = 'navbar-default',choices = NAVCOLORES_CHOICES)
    sidebar_grid = models.CharField(max_length=20,verbose_name="grid menu", default = 'a',choices = SIDEBAR_CHOICES)
    tinte = models.CharField(max_length=20,verbose_name="tinte", default = 'a',choices = TINTE_CHOICES)
    font = models.CharField(max_length=70,verbose_name="font", default = 'a',choices = FONT_CHOICES)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    
    def __str__(self):
        return self.schema_name
        
class Dominio(DomainMixin):
    pass

class TenantInactivo(models.Model):
    id_tenant = models.IntegerField(null=True,blank=True)
    url = models.CharField(max_length=200, null=True, default="")
    class Meta:
		db_table = 'TenantInactivo'

class Administrador_tenants(User):
    
    
    IDENTIFICACION_CHOICES = (('CC','Cedula de ciudadania'),('TI','Tarjeta de identidad'),('CE','Cedula de extranjeria'))
    ESTADO_CHOICES = (('ACTIVO','Activo'),('INACTIVO','Inactivo'))
    
    fecha_nacimiento = models.DateField(verbose_name="fecha de nacimiento")
    tipo_documento_identificacion = models.CharField(max_length=20,verbose_name="tipo de identificacion",choices = IDENTIFICACION_CHOICES)
    numero_documento_identificacion = models.CharField(max_length=20,verbose_name="numero de documento de identificacion")	
    correo_electronico = models.EmailField(verbose_name="correo electronico")
    telefono = models.CharField(max_length=20,verbose_name="numero telefonico")
    estado = models.CharField(max_length=20,verbose_name="estado",default = 'ACTIVO',choices = ESTADO_CHOICES)
    primer_nombre = models.CharField(max_length=100,verbose_name="primer nombre")
    segundo_nombre = models.CharField(max_length=100,verbose_name="segundo nombre")
    primer_apellido = models.CharField(max_length=100,verbose_name="primer apellido")
    segundo_apellido = models.CharField(max_length=100,verbose_name="segundo apellido")


    def __str__(self):	
        return '%s %s %s %s' % (self.primer_nombre , self.segundo_nombre , self.primer_apellido , self.segundo_apellido)
		
    def nombre(self):	
        return '%s %s %s %s' % (self.primer_nombre , self.segundo_nombre , self.primer_apellido , self.segundo_apellido)
	
	class Meta:
		db_table = 'usuario_administrador_tenants'