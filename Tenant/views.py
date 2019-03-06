from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.db import connection
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView, UpdateView
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group,Permission
from Usuario.permisos_usuarios import *
from django.contrib.auth.models import User
from pizzeria.utils import (tenant_context, schema_exists,get_public_schema_name)

from Usuario.models import Administrador, Usuario, Cliente
from django.db.models import Max
from .permisos_usuarios import *
from Usuario.views import auxiliar
from django.test import RequestFactory
from Vents.models import Carrito
import  simplejson
# from .utilities import obtener_todos_mensajes

# Create your views here.


def loginIn(request):

	if request.method == 'POST':

		usuario = request.POST['correo']
		clave = request.POST['password']

		user = authenticate(username=usuario, password=clave)
		if user is not None:

			if user.is_active:

				login(request, user)

				return HttpResponseRedirect(reverse("listar_tenant"))

			else:

				messages.warning(request, 'No esta activado este usuario por favor hablar con un administrador')
				print "No esta activo"
				return render(request, "login_tenant.html")

		else:

			username = None
			if request.user.is_authenticated():
				username = request.user.username

			messages.warning(request, 'Hubo un problema con el usuario y/o contrasena')
			return render(request, "login_tenant.html", {"usuario" : username})

	else:
		username = None
		if request.user.is_authenticated():
			username = request.user.username
		return render(request, "login_tenant.html", {'usuario' : username })

def index_tenant(request):
	dominios = Dominio.objects.all()
	dominios_https = []

	for dominio in dominios:
		if not dominio.domain == "pizzeria-matt9742.c9users.io":
			id = dominio.tenant_id
			franquicia = Franquicia.objects.get(id=id)

			if franquicia.estado == 'ACTIVO':
				pareja = []
				subdominio = dominio.domain.split(".")[0]
				pareja.append(subdominio)
				pareja.append("https://"+dominio.domain)
				dominios_https.append(pareja)


	print dominios_https
	return render(request, 'landing_tenant.html', {'dominios': dominios_https})

#@login_required(login_url='/loginIn/')
class TenantCreateView(CreateView):
    model = Franquicia
    fields = ['nombre', 'descripcion', 'estado', 'reportes_graficos', 'color' , 'nav_var_color', 'sidebar_grid', 'tinte', 'font']
    success_url = '/registrar-tenant'

    
    def form_valid(self,form):


        tenant_registrado = form.instance
        tenant_registrado.schema_name = tenant_registrado.nombre.lower() #convert to lowercase
        self.object = form.save()

        dominio_tenant = Dominio(domain=self.object.nombre.lower() +'.pizzeria-matt9742.c9users.io',
                                is_primary=True,
                                tenant_id=tenant_registrado.id
                                )

        dominio_tenant.save()
        print ("--------......Aqui empieza lo buenooo:....---------")
        previous_tenant = connection.tenant
        print ("--------Aqui empieza se va a imprimir :---------")
        print previous_tenant

        try:
        	connection.set_schema(self.object.nombre.lower())
        	print ("------------------desde el tenant---------------")
        	nuevotenant = connection.tenant
        	print (nuevotenant)
        	print ("------------------usuarios---------------")
        	usuario = Administrador(user_ptr_id=1 ,fecha_nacimiento = '1997-02-02' , tipo_documento_identificacion = 'CC', numero_documento_identificacion='root',
        	correo_electronico = 'root@correo.com', telefono ='11111',estado = 'ACTIVO', primer_nombre = self.object.nombre, primer_apellido ='root', password= 'root', username = self.object.nombre + 'root',
        	segundo_nombre = 'root')
        	usuario.save()

        	clinte = Cliente(user_ptr_id=2 ,fecha_nacimiento = '2000-02-02' , tipo_documento_identificacion = 'CC', numero_documento_identificacion='default',
        	correo_electronico = 'default@correo.com', telefono ='11111',estado = 'ACTIVO', primer_nombre = 'default', primer_apellido ='default', password= 'default', username = 'default',
        	segundo_nombre = 'default', tarjeta_credito = '999999999')
        	clinte.save()
        	canasta = Carrito(usuario=clinte)
        	canasta.save()

        	#request_factory = RequestFactory()

        	#request1 = request_factory.get('/path', data={'COOKIES': "ADSA"})
        	#configurar_permisos_view(self,request1)

        	#aux = auxiliar()
        	#aux.imprimir()
        	#aux.configurar_permisos_viewe()

        	#print ("-----------------------------------------")



        	#admin = Administrador(usuario_ptr_id=1)
        	#admin.save()
        	#maximo = Usuario.objects.all().aggregate(Max('user_ptr_id'))
        	#print maximoq
    	finally:
    		print ("este paso termina aqui.")
    		connection.set_schema("public") # algo
    		print ("este paso cheeee.")



        return super(TenantCreateView, self).form_valid(form)
       # with schema_context(self.object.nombre):
       # 	print ("--------preparalityyyyy-------------------")
        #	maximo = buga.Usuario.objects.all().aggregate(Max('user_ptr_id'))
    	#	print ("------------------------")
    	#	print maximo

#@login_required(login_url='/loginIn/')
def modificar_tenant_view(request,id_tenant,tenant_form, domain_form):

	franquicia = get_object_or_404(Franquicia,id=id_tenant)
	dominio = get_object_or_404(Dominio, tenant=id_tenant)

	if request.method == 'POST':

		franquicia_form = tenant_form(request.POST,instance=franquicia)
		dominio_form = domain_form(request.POST,instance=dominio)


		if franquicia_form.is_valid():
			franquicia_form.save()
			dominio.domain = franquicia_form.cleaned_data['nombre'].lower() +'.pizzeria-matt9742.c9users.io'
			dominio.save()
			return HttpResponseRedirect(reverse('listar_tenant'))
			

	franquicia_form  = tenant_form(instance=franquicia)
	dominio_form  = domain_form(instance=dominio)

	return render(request, 'franquicia_form_2.html', {'franquicia_form':franquicia_form})


@login_required(login_url='/loginIn/')
def desactivar_tenant_view(request,id_tenant):

	franquicia = get_object_or_404(Franquicia,id=id_tenant)

	franquicia.estado = 'INACTIVO'
	franquicia.save()

	return HttpResponseRedirect(reverse("listar_tenant"))

#@login_required(login_url='/loginIn/')
class DesactivarTenant(TemplateView):
	
	@login_required(login_url='/loginIn/')
	def post(self,request,*args,**kwargs):
		if "codigoTenant" in request.POST:
			try:
				codigoTenant = request.POST['codigoTenant']
				franquicia = get_object_or_404(Franquicia,id=codigoTenant)
				franquicia.estado = 'INACTIVO'
				franquicia.save()
				dominio = get_object_or_404(Dominio,id=codigoTenant)
				inactivado = TenantInactivo(id_tenant=codigoTenant, url=dominio.domain)
				inactivado.save()
				dominio.domain=""
				dominio.save()
				mensaje = {'status':'True','codigoTenant':codigoTenant}
			except:
				mensaje = {'status':'False'}
			response = simplejson.dumps(mensaje)
			return HttpResponse(response ,content_type='application/json')


class ActivarTenant(TemplateView):
	
	@login_required(login_url='/loginIn/')
	def post(self,request,*args,**kwargs):
		if "codigoTenant" in request.POST:
			try:
				codigoTenant = request.POST['codigoTenant']
				franquicia = get_object_or_404(Franquicia,id=codigoTenant)
				franquicia.estado = 'ACTIVO'
				franquicia.save()
				dominio = get_object_or_404(Dominio,id=codigoTenant)
				inactivado = TenantInactivo.objects.get(id_tenant=codigoTenant)
				dominio.domain=inactivado.url
				dominio.save()
				inactivado.delete()
				mensaje = {'status':'True','codigoTenant':codigoTenant}
			except:
				mensaje = {'status':'False'}
			response = simplejson.dumps(mensaje)
			return HttpResponse(response ,content_type='application/json')


@login_required(login_url='/loginIn/')
def activar_tenant_view(request,id_tenant):

	franquicia = get_object_or_404(Franquicia,id=id_tenant)

	franquicia.estado = 'ACTIVO'
	franquicia.save()

	return HttpResponseRedirect(reverse("listar_tenant"))


@login_required(login_url='/loginIn/')
def listar_tenant_view(request):
	franquicias = Franquicia.objects.all()
	dominios = Dominio.objects.all()
	dicc = {}
	inactivos= TenantInactivo.objects.all()
	for franquicia in franquicias:
	    dominio = dominios.filter(tenant_id=franquicia.id)
	    dicc['' + franquicia.nombre] = dominio[0].domain

	return render(request, 'listar_tenant.html', {'franquicias': franquicias, 'dominios' : dicc, 'inactivos':inactivos})

#USUARIO ADMINISTRADOR 2.0
#Class encargado de crear usuario administrador
#@login_required(login_url='/loginIn/')
class CrearUsuarioAdministradorTenant(TemplateView):

    #@login_required(login_url='/loginIn/')
    def get(self,request,*args,**kwargs):
    	return render_to_response('formulario_crear_administrador_tenant.html',{},
    			context_instance=RequestContext(request))

    #@login_required(login_url='/loginIn/')
    def post(self,request,*args,**kwargs):

    	#print request.POST
        nombres = request.POST['nombre']
        primer_apellido = request.POST['PrimerApellido']
        segundo_apellido = request.POST['SegundoApellido']
        tipo_identidad = request.POST['tipoIdentidad[]']
        numero_identificacion = request.POST['NumeroIdentificacion']
        fecha_nacimiento = request.POST['FechaNacimiento']
        inputEmail = request.POST['inputEmail']
        telefono = request.POST['Telefono']
        inputPassword = request.POST['inputPassword']


        try:
            usuario = Administrador_tenants.objects.get(correo_electronico=inputEmail)
            mensaje = "Ya existe el Usuario con ese EMAIL"
            messages.info(request,mensaje)

            return render_to_response('formulario_crear_administrador_tenant.html',{},
            context_instance=RequestContext(request))

        except:

        	try:
        		usuario = Administrador_tenants.objects.get(numero_documento_identificacion=numero_identificacion)
        		mensaje = "Ya existe el Usuario con este Numero de Identificacion"
        		messages.error(request,mensaje)

        		return render_to_response('formulario_crear_administrador_tenant.html',{},
        		context_instance=RequestContext(request))

        	except:


        		try:

		            usuario = Administrador_tenants(fecha_nacimiento=fecha_nacimiento, numero_documento_identificacion=numero_identificacion, correo_electronico=inputEmail, telefono=telefono, primer_nombre=nombres,
		            primer_apellido=primer_apellido, segundo_apellido=segundo_apellido, tipo_documento_identificacion= tipo_identidad, username = inputEmail)
		            usuario.save()
		            usuario.set_password(inputPassword)
		            usuario.save()

		            mensaje = "El usuario se registro con exito"
		            messages.info(request,mensaje)


		            return HttpResponseRedirect(reverse("usuario:listar_usuario"))

		    	except:

		    		mensaje = "El Password es muy similar al Nombre, Apellidos, digite uno mas complicado"
	        		messages.error(request,mensaje)

	        		return render_to_response('formulario_crear_administrador_tenant.html',{},
	        		context_instance=RequestContext(request))

#Class encargada de Modificar Usuario
#@login_required(login_url='/loginIn/')
class ModificarUsuario(TemplateView):
    @login_required(login_url='/loginIn/')
    def get(self,request,*args,**kwargs):

    	id = kwargs['id_usuario']
    	usuario = Administrador_tenants.objects.get(id=id)

    	return render_to_response('formulario_modificar_administrador_tenant.html',{'usuario':usuario},
			context_instance=RequestContext(request))

	@login_required(login_url='/loginIn/')
	def post(self,request,*args,**kwargs):

		nombres = request.POST['nombre']
		primer_apellido = request.POST['PrimerApellido']
		segundo_apellido = request.POST['SegundoApellido']
		tipo_identidad = request.POST['tipoIdentidad[]']
		numero_identificacion = request.POST['NumeroIdentificacion']
		telefono = request.POST['Telefono']

		id = kwargs['id_usuario']
		usuario = Administrador_tenants.objects.get(id=id)
		usuario.primer_nombre = nombres
		usuario.primer_apellido = primer_apellido
		usuario.segundo_apellido = segundo_apellido
		usuario.tipo_documento_identificacion = tipo_identidad
		usuario.numero_documento_identificacion = numero_identificacion
		usuario.telefono = telefono

		usuario.save()


		return HttpResponseRedirect(reverse("listar_usuario_administrador"))

#@login_required()
@login_required(login_url='/loginIn/')
def eliminar_usuario_view(request,id_usuario,modelo):
	usuario = get_object_or_404(modelo,id = id_usuario)
	usuario.estado = 'INACTIVO'
	usuario.save()

	return listar_usuario_tenant_view(request)

#@login_required()
@login_required(login_url='/loginIn/')
def activar_usuario_view(request,id_usuario,modelo):
	usuario = get_object_or_404(modelo,id = id_usuario)
	usuario.estado = 'ACTIVO'
	usuario.save()

	return listar_usuario_tenant_view(request)

@login_required(login_url='/loginIn/')
def listar_usuario_tenant_view(request):
	lista = Administrador_tenants.objects.all()
	return render(request, 'listar_usuarios_tenant.html', {'lista':lista})


def configurar_permisos_view(request):

	grupo_administrador_tenant, grupo_administrador__tenant_creado = Group.objects.get_or_create(name="AdministradorTenant")

	permisos_administrador = Permission.objects.filter(codename__in=PERMISOS_ADMINISTADOR_TENANTS)
	grupo_administrador_tenant.permissions.set(permisos_administrador)

	return HttpResponse("Permisos Actualizados")


@login_required(login_url='/loginIn/')
def visualizar_administrador_view(request,id_usuario,modelo):

	usuario = get_object_or_404(modelo,id=id_usuario)
	return render(request, 'perfil_administrador.html', {'usuario':usuario})