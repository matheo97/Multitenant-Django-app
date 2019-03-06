from django.shortcuts import render_to_response, render
from django.template import RequestContext
from .forms import *
from .models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse	
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group,Permission
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max
import json
from django.contrib import messages
from .permisos_usuarios import *

# EMAIL IMPORT

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from pizzeria.settings import DEFAULT_FROM_EMAIL
from django.views.generic import *
from .forms import PasswordResetRequestForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from Tenant.models import Franquicia

from django.utils.decorators import method_decorator


#Class encargado de crear usuario administrador
class CrearUsuarioAdministrador(TemplateView):
    
    def get(self,request,*args,**kwargs):
    	return render_to_response('formulario_crear_administrador.html',{},
    			context_instance=RequestContext(request))
			
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
            usuario = Usuario.objects.get(correo_electronico=inputEmail)
            mensaje = "Ya existe el Usuario con ese EMAIL"
            messages.info(request,mensaje)
            
            return render_to_response('formulario_crear_administrador.html',{},
            context_instance=RequestContext(request))
            
        except:
        	
        	try:
        		usuario = Usuario.objects.get(numero_documento_identificacion=numero_identificacion)
        		mensaje = "Ya existe el Usuario con este Numero de Identificacion"
        		messages.error(request,mensaje)
        		
        		return render_to_response('formulario_crear_administrador.html',{},
        		context_instance=RequestContext(request))
        		
        	except:
        		
        		
        		try:
	                
		            usuario = Administrador(fecha_nacimiento=fecha_nacimiento, numero_documento_identificacion=numero_identificacion, correo_electronico=inputEmail, telefono=telefono, primer_nombre=nombres,
		            primer_apellido=primer_apellido, segundo_apellido=segundo_apellido, tipo_documento_identificacion= tipo_identidad, username = inputEmail)
		            
		            usuario.save()
		            usuario.groups.add(Group.objects.get(name="Administrador"))
		            
		            mensaje = "El usuario se registro con exito"
		            messages.info(request,mensaje)
		            
		            
		            return HttpResponseRedirect(reverse("usuario:listar_usuario"))
		    	
		    	except:
		    		
		    		mensaje = "El Password es muy similar al Nombre, Apellidos, digite uno mas complicado"
	        		messages.error(request,mensaje)
	        		
	        		return render_to_response('formulario_crear_administrador.html',{},
	        		context_instance=RequestContext(request))
	        		
	        		
	        		
#Class encargada de Crear Digitador	        		
class CrearUsuarioDigitador(TemplateView):
    
    def get(self,request,*args,**kwargs):
    	return render_to_response('formulario_crear_digitador.html',{},
    			context_instance=RequestContext(request))
			
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
            usuario = Usuario.objects.get(correo_electronico=inputEmail)
            mensaje = "Ya existe el Usuario con ese EMAIL"
            messages.info(request,mensaje)
            
            return render_to_response('formulario_crear_digitador.html',{},
            context_instance=RequestContext(request))
        
       
        except:
        	
        	
        	try:
        		usuario = Usuario.objects.get(numero_documento_identificacion=numero_identificacion)
        		mensaje = "Ya existe el Usuario con este Numero de Identificacion"
        		messages.error(request,mensaje)
        		
        		return render_to_response('formulario_crear_digitador.html',{},
        		context_instance=RequestContext(request))
        		
        	except:
        		
	                print "Va a crear el dijita"
	    			
	    			
	    			usuario = Digitador(fecha_nacimiento=fecha_nacimiento, numero_documento_identificacion=numero_identificacion, correo_electronico=inputEmail, telefono=telefono, primer_nombre=nombres,primer_apellido=primer_apellido, segundo_apellido=segundo_apellido, tipo_documento_identificacion= tipo_identidad, username = inputEmail)
	    			usuario.save()

	    			usuario.groups.add(Group.objects.get(name="Digitador"))
	    			
	    			mensaje = "El usuario se registro con exito"
	    			messages.info(request,mensaje)
	    			
	    			return HttpResponseRedirect(reverse("usuario:listar_usuario"))
		    	
		    	except:
		    		
		    		mensaje = "El Password es muy similar al Nombre, Apellidos, digite uno mas complicado"
	        		messages.error(request,mensaje)
	        		
	        		return render_to_response('formulario_crear_digitador.html',{},
	        		context_instance=RequestContext(request))
	


#Class encargada de Crear Cliente        		
class CrearUsuarioCliente(TemplateView):
    
    def get(self,request,*args,**kwargs):
    	return render_to_response('formulario_crear_cliente.html',{},
    			context_instance=RequestContext(request))
			
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
        tarjeta_credito = request.POST['tarjeta_credito']
        
        	
        try:
            usuario = Usuario.objects.get(correo_electronico=inputEmail)
            mensaje = "Ya existe el Usuario con ese EMAIL"
            messages.info(request,mensaje)
            
            return render_to_response('formulario_crear_cliente.html',{},
            context_instance=RequestContext(request))
            
        except:
        	
        	try:
        		usuario = Usuario.objects.get(numero_documento_identificacion=numero_identificacion)
        		mensaje = "Ya existe el Usuario con este Numero de Identificacion"
        		messages.error(request,mensaje)
        		
        		return render_to_response('formulario_crear_cliente.html',{},
        		context_instance=RequestContext(request))
        		
        	except:
        		
        		
        		try:
	                
		            usuario = Cliente(fecha_nacimiento=fecha_nacimiento, numero_documento_identificacion=numero_identificacion, correo_electronico=inputEmail, telefono=telefono, primer_nombre=nombres,
		            primer_apellido=primer_apellido, segundo_apellido=segundo_apellido, tipo_documento_identificacion= tipo_identidad, username = inputEmail, tarjeta_credito = tarjeta_credito)
		            
		            usuario.save()
		            usuario.groups.add(Group.objects.get(name="Cliente"))
	
		            mensaje = "El usuario se registro con exito"
		            messages.info(request,mensaje)
		            
		            
		            return HttpResponseRedirect(reverse("usuario:listar_usuario"))
		    	
		    	except:
		    		
		    		mensaje = "El Password es muy similar al Nombre, Apellidos, digite uno mas complicado"
	        		messages.error(request,mensaje)
	        		
	        		return render_to_response('formulario_crear_cliente.html',{},
	        		context_instance=RequestContext(request))
	        		
#PERMISOS USUARIOS
def configurar_permisos_view(request):

	grupo_administrador, grupo_administrador_creado = Group.objects.get_or_create(name="Administrador")
	grupo_digitador, grupo_digitador_creado = Group.objects.get_or_create(name="Digitador")
	grupo_cliente, grupo_cliente_creado = Group.objects.get_or_create(name="Cliente")
	

	permisos_administrador = Permission.objects.filter(codename__in=PERMISOS_ADMINISTRADOR)
	grupo_administrador.permissions.set(permisos_administrador)

	permisos_digitador = Permission.objects.filter(codename__in=PERMISOS_DIGITADOR)
	grupo_digitador.permissions.set(permisos_digitador)

	permisos_cliente = Permission.objects.filter(codename__in=PERMISOS_CLIENTE)
	grupo_cliente.permissions.set(permisos_cliente)



	return HttpResponse("Permisos Actualizados")
	
	
	
#@login_required()
def modificar_usuario_view(request,id_usuario,clase_form,modelo):
	
	usuario = get_object_or_404(modelo,id=id_usuario)
	
	if request.method == 'POST':

		form = clase_form(request.POST,instance=usuario)		

		if form.is_valid():
			form.save()			
			return HttpResponseRedirect(reverse("usuario:listar_usuario"))
		
	form = clase_form(instance=usuario)
	
	return render(request, 'formulario_modificar_administrador.html', {'form':form})
	
	

#Class encargada de Modificar Usuario        		
class ModificarUsuario(TemplateView):
    
    def get(self,request,*args,**kwargs):
    	
    	print kwargs
    	id = kwargs['id_usuario']
    	usuario = Usuario.objects.get(id=id)
    	
    	if kwargs['modelo'] == 'Digitador':
    		return render_to_response('formulario_modificar_digitador.html',{'usuario':usuario},
    			context_instance=RequestContext(request))
    			
    	elif kwargs['modelo'] == 'Administrador':
    		return render_to_response('formulario_modificar_administrador.html',{'usuario':usuario},
    			context_instance=RequestContext(request))
    	else:
    		usuarioCliente = Cliente.objects.get(id=id)
    		return render_to_response('formulario_modificar_cliente.html',{'usuario':usuario, 'tarjeta_credito': usuarioCliente.tarjeta_credito},
    			context_instance=RequestContext(request))
			
    def post(self,request,*args,**kwargs):
    	
    	print request.POST
        nombres = request.POST['nombre']
        primer_apellido = request.POST['PrimerApellido']
        segundo_apellido = request.POST['SegundoApellido']
        tipo_identidad = request.POST['tipoIdentidad[]']
        numero_identificacion = request.POST['NumeroIdentificacion']
        fecha_nacimiento = request.POST['FechaNacimiento']
        inputEmail = request.POST['inputEmail']
        telefono = request.POST['Telefono']
        inputPassword = request.POST['inputPassword']
        tarjeta_credito = request.POST['tarjeta_credito']
        
        	
        try:
            usuario = Usuario.objects.get(correo_electronico=inputEmail)
            mensaje = "Ya existe el Usuario con ese EMAIL"
            messages.info(request,mensaje)
            
            return render_to_response('formulario_crear_cliente.html',{},
            context_instance=RequestContext(request))
            
        except:
        	
        	try:
        		usuario = Usuario.objects.get(numero_documento_identificacion=numero_identificacion)
        		mensaje = "Ya existe el Usuario con este Numero de Identificacion"
        		messages.error(request,mensaje)
        		
        		return render_to_response('formulario_crear_cliente.html',{},
        		context_instance=RequestContext(request))
        		
        	except:
        		
        		
        		try:
	                
		            usuario = Cliente(fecha_nacimiento=fecha_nacimiento, numero_documento_identificacion=numero_identificacion, correo_electronico=inputEmail, telefono=telefono, primer_nombre=nombres,
		            primer_apellido=primer_apellido, segundo_apellido=segundo_apellido, tipo_documento_identificacion= tipo_identidad, username = inputEmail, tarjeta_credito = tarjeta_credito)
		            
		            usuario.save()
		            usuario.groups.add(Group.objects.get(name="Cliente"))
	
		            mensaje = "El usuario se registro con exito"
		            messages.info(request,mensaje)
		            
		            
		            return HttpResponseRedirect(reverse("usuario:listar_usuario"))
		    	
		    	except:
		    		
		    		mensaje = "El Password es muy similar al Nombre, Apellidos, digite uno mas complicado"
	        		messages.error(request,mensaje)
	        		
	        		return render_to_response('formulario_crear_cliente.html',{},
	        		context_instance=RequestContext(request))
	
	
	
	
	
#@login_required()
def visualizar_usuario_view(request,id_usuario,modelo):
	
	usuario = get_object_or_404(modelo,id=id_usuario)
	return render(request, 'perfil_usuario.html', {'usuario':usuario})
	



#@login_required()
def listar_usuario_view(request):
	lista = User.objects.all()
	print(lista)
	return render(request, 'listar_usuarios.html', {'lista':lista})
	
	
	

#@login_required()
def eliminar_usuario_view(request,id_usuario,modelo):
	usuario = get_object_or_404(Usuario,id = id_usuario)
	usuario.estado = 'INACTIVO'
	usuario.save()

	return listar_usuario_view(request)
	
	
#@login_required()
def activar_usuario_view(request,id_usuario,modelo):
	usuario = get_object_or_404(Usuario,id = id_usuario)
	usuario.estado = 'ACTIVO'
	usuario.save()

	return listar_usuario_view(request)
	
	

@csrf_exempt
def actualizar_lista_usuarios(request):
	
	print(request.GET)
	select_cargo = request.GET['select_cargo']
	select_disponibilidad = request.GET['select_disponibilidad']
	dicc = {}
	resultados = consulta_lista_usuarios(select_cargo, select_disponibilidad)
	
	
	# print resultados
	
	# digitadores = Digitador.objects.all()
	# usuario_temp = get_object_or_404(Usuario,id = digitadores[0].id)
	# user_temp = get_object_or_404(User,id = digitadores[0].id)
	
	# dicc = {}
	# dicc["id"] = str(usuario_temp.id)
	# dicc["nombre"] = str(usuario_temp.nombre)
	# dicc["cargo"] = 'Administrador'
	# dicc["username"] = str(user_temp.username)
	
	data=json.dumps(resultados)
	mimetype="application/json"
	return HttpResponse(data,mimetype)
	
	
def consulta_lista_usuarios(tipo, disponibilidad):
	
	resultado = []
	
	if(tipo == 'Todos'):
		
		print "holi1"
		
		administradores = Administrador.objects.all()
		digitadores = Digitador.objects.all()
		clientes = Cliente.objects.all()
		
		for administrador in administradores:
			user_temp = get_object_or_404(User,id = administrador.id)
			usuario_temp = get_object_or_404(Usuario,id = administrador.id)
			
			if disponibilidad == 'Todos':
				dicc = {}
				dicc["id"] = str(usuario_temp.id)
				dicc["nombre"] = str(usuario_temp.nombre)
				dicc["cargo"] = 'Administrador'
				dicc["username"] = str(user_temp.username)
				dicc["estado"] = str(usuario_temp.estado)
				
				resultado.append(dicc)
				
			if disponibilidad == 'Activos':
				if usuario_temp.estado == 'ACTIVO':
					dicc = {}
					dicc["id"] = str(usuario_temp.id)
					dicc["nombre"] = str(usuario_temp.nombre)
					dicc["cargo"] = 'Administrador'
					dicc["username"] = str(user_temp.username)
					dicc["estado"] = str(usuario_temp.estado)
					
					resultado.append(dicc)
			
			if disponibilidad == 'Inactivos':
				if usuario_temp.estado == 'INACTIVO':
					dicc = {}
					dicc["id"] = str(usuario_temp.id)
					dicc["nombre"] = str(usuario_temp.nombre)
					dicc["cargo"] = 'Administrador'
					dicc["username"] = str(user_temp.username)
					dicc["estado"] = str(usuario_temp.estado)
					
					resultado.append(dicc)
					
		for digitador in digitadores:
			user_temp = get_object_or_404(User,id = digitador.id)
			usuario_temp = get_object_or_404(Usuario,id = digitador.id)
			
			if disponibilidad == 'Todos':
				dicc = {}
				dicc["id"] = str(usuario_temp.id)
				dicc["nombre"] = str(usuario_temp.nombre)
				dicc["cargo"] = 'Digitador'
				dicc["username"] = str(user_temp.username)
				dicc["estado"] = str(usuario_temp.estado)
				
				resultado.append(dicc)
			
			
			if disponibilidad == 'Activos':
				if usuario_temp.estado == 'ACTIVO':
					dicc = {}
					dicc["id"] = str(usuario_temp.id)
					dicc["nombre"] = str(usuario_temp.nombre)
					dicc["cargo"] = 'Digitador'
					dicc["username"] = str(user_temp.username)
					dicc["estado"] = str(usuario_temp.estado)
					
					resultado.append(dicc)
					
			
			if disponibilidad == 'Inactivos':
				if usuario_temp.estado == 'INACTIVO':
					dicc = {}
					dicc["id"] = str(usuario_temp.id)
					dicc["nombre"] = str(usuario_temp.nombre)
					dicc["cargo"] = 'Digitador'
					dicc["username"] = str(user_temp.username)
					dicc["estado"] = str(usuario_temp.estado)
					
					resultado.append(dicc)
					
		for cliente in clientes:
			user_temp = get_object_or_404(User,id = cliente.id)
			usuario_temp = get_object_or_404(Usuario,id = cliente.id)
			
			if disponibilidad == 'Todos':
				dicc = {}
				dicc["id"] = str(usuario_temp.id)
				dicc["nombre"] = str(usuario_temp.nombre)
				dicc["cargo"] = 'Cliente'
				dicc["username"] = str(user_temp.username)
				dicc["estado"] = str(usuario_temp.estado)
				
				resultado.append(dicc)
			
			if disponibilidad == 'Activos':
				if usuario_temp.estado == 'ACTIVO':
					dicc = {}
					dicc["id"] = str(usuario_temp.id)
					dicc["nombre"] = str(usuario_temp.nombre)
					dicc["cargo"] = 'Cliente'
					dicc["username"] = str(user_temp.username)
					dicc["estado"] = str(usuario_temp.estado)
					
					resultado.append(dicc)
			
			if disponibilidad == 'Inactivos':
				if usuario_temp.estado == 'INACTIVO':
					dicc = {}
					dicc["id"] = str(usuario_temp.id)
					dicc["nombre"] = str(usuario_temp.nombre)
					dicc["cargo"] = 'Cliente'
					dicc["username"] = str(user_temp.username)
					dicc["estado"] = str(usuario_temp.estado)
					
					resultado.append(dicc)
					
		print resultado
		
	elif(tipo == 'Administradores'):
		print "holi2"
		
		for administrador in administradores:
			user_temp = get_object_or_404(User,id = administrador.id)
			usuario_temp = get_object_or_404(Usuario,id = administrador.id)
			
			if disponibilidad == 'Todos':
				dicc = {}
				dicc["id"] = usuario_temp.id
				dicc["nombre"] = usuario_temp.nombre
				dicc["cargo"] = 'Administrador'
				dicc["username"] = user_temp.username
				dicc["estado"] = str(usuario_temp.estado)
				
				resultado.append(dicc)
			
			if disponibilidad == 'Activos':
				if usuario_temp.estado == 'ACTIVO':
					dicc = {}
					dicc["id"] = usuario_temp.id
					dicc["nombre"] = usuario_temp.nombre
					dicc["cargo"] = 'Administrador'
					dicc["username"] = user_temp.username
					dicc["estado"] = str(usuario_temp.estado)
					
					resultado.append(dicc)
			
			if disponibilidad == 'Inactivos':
				if usuario_temp.estado == 'INACTIVO':
					dicc = {}
					dicc["id"] = usuario_temp.id
					dicc["nombre"] = usuario_temp.nombre
					dicc["cargo"] = 'Administrador'
					dicc["username"] = user_temp.username
					dicc["estado"] = str(usuario_temp.estado)
					
					resultado.append(dicc)
	
	elif(tipo == 'Digitadores'):
		print "holi3"
		
		for digitador in digitadores:
			user_temp = get_object_or_404(User,id = digitador.id)
			usuario_temp = get_object_or_404(Usuario,id = digitador.id)
			
			if disponibilidad == 'Todos':
				dicc = {}
				dicc["id"] = str(usuario_temp.id)
				dicc["nombre"] = str(usuario_temp.nombre)
				dicc["cargo"] = 'Digitador'
				dicc["username"] = str(user_temp.username)
				dicc["estado"] = str(usuario_temp.estado)
				
				resultado.append(dicc)
			
			
			if disponibilidad == 'Activos':
				if usuario_temp.estado == 'ACTIVO':
					dicc = {}
					dicc["id"] = str(usuario_temp.id)
					dicc["nombre"] = str(usuario_temp.nombre)
					dicc["cargo"] = 'Digitador'
					dicc["username"] = str(user_temp.username)
					dicc["estado"] = str(usuario_temp.estado)
					
					resultado.append(dicc)
			
			if disponibilidad == 'Inactivos':
				if usuario_temp.estado == 'INACTIVO':
					dicc = {}
					dicc["id"] = str(usuario_temp.id)
					dicc["nombre"] = str(usuario_temp.nombre)
					dicc["cargo"] = 'Digitador'
					dicc["username"] = str(user_temp.username)
					dicc["estado"] = str(usuario_temp.estado)
					
					resultado.append(dicc)
		
	elif(tipo == 'Clientes'):
		print "holi4"
		
		for cliente in clientes:
			user_temp = get_object_or_404(User,id = cliente.id)
			usuario_temp = get_object_or_404(Usuario,id = cliente.id)
			
			if disponibilidad == 'Todos':
				dicc = {}
				dicc["id"] = str(usuario_temp.id)
				dicc["nombre"] = str(usuario_temp.nombre)
				dicc["cargo"] = 'Cliente'
				dicc["username"] = str(user_temp.username)
				dicc["estado"] = str(usuario_temp.estado)
				
				resultado.append(dicc)
			
			if disponibilidad == 'Activos':
				if usuario_temp.estado == 'ACTIVO':
					dicc = {}
					dicc["id"] = str(usuario_temp.id)
					dicc["nombre"] = str(usuario_temp.nombre)
					dicc["cargo"] = 'Cliente'
					dicc["username"] = str(user_temp.username)
					dicc["estado"] = str(usuario_temp.estado)
					
					resultado.append(dicc)
			
			if disponibilidad == 'Inactivos':
				if usuario_temp.estado == 'INACTIVO':
					dicc = {}
					dicc["id"] = str(usuario_temp.id)
					dicc["nombre"] = str(usuario_temp.nombre)
					dicc["cargo"] = 'Cliente'
					dicc["username"] = str(user_temp.username)
					dicc["estado"] = str(usuario_temp.estado)
					
					resultado.append(dicc)
		
	
	return resultado
	
	
	
	
	
class ResetPasswordRequestView(FormView):
    template_name = "account/test_template.html"    #code for template is given below the view's code
    success_url = '/account/login'
    form_class = PasswordResetRequestForm

    @staticmethod
    def validate_email_address(email):
	    '''
	    This method here validates the if the input is an email address or not. Its return type is boolean, True if the input is a email address or False if its not.
	    '''
	    try:
	    	validate_email(email)
	    	return True
	    except ValidationError:
	    	return False
    
    def post(self, request, *args, **kwargs):
	    '''
	    A normal post request which takes input from field "email_or_username" (in ResetPasswordRequestForm). 
	    '''
	    
	    form = self.form_class(request.POST)
	    
	    if form.is_valid():
	    	data= form.cleaned_data["email_or_username"]
	    
	    
	    if self.validate_email_address(data) is True:                 #uses the method written above
	    	'''
	    	If the input is an valid email address, then the following code will lookup for users associated with that email address. If found then an email will be sent to the address, else an error message will be printed on the screen.
	    	'''
	    	associated_users= User.objects.filter(Q(email=data)|Q(username=data))
	    	
	    	if associated_users.exists():
	    		
	    		for user in associated_users:
	    			c = {
	    					'email': user.email,
	    					'domain': request.META['HTTP_HOST'],
	    					'site_name': 'your site',
	    					'uid': urlsafe_base64_encode(force_bytes(user.pk)),
	    					'user': user,
	    					'token': default_token_generator.make_token(user),
	    					'protocol': 'http',
	    				
	    			}
    				subject_template_name='registration/password_reset_subject.txt' 
    				# copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
    				email_template_name='registration/password_reset_email.html'
    				# copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
    				subject = loader.render_to_string(subject_template_name, c)
    				# Email subject *must not* contain newlines
    				subject = ''.join(subject.splitlines())
    				email = loader.render_to_string(email_template_name, c)
    				send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
	                result = self.form_valid(form)
	                messages.success(request, 'An email has been sent to ' + data +". Please check its inbox to continue reseting password.")
	                
	                return result
	                
		        result = self.form_invalid(form)
		        messages.error(request, 'No user is associated with this email address')
		        return result
	        
	        
	        else:
	        
			'''
			If the input is an username, then the following code will lookup for users associated with that user. If found then an email will be sent to the user's address, else an error message will be printed on the screen.
			'''
			
			associated_users= User.objects.filter(username=data)
			if associated_users.exists():
				for user in associated_users:
					c = {
                        'email': user.email,
                        'domain': 'example.com', #or your domain
                        'site_name': 'example',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                        }
					subject_template_name='registration/password_reset_subject.txt'
					email_template_name='registration/password_reset_email.html'
					subject = loader.render_to_string(subject_template_name, c)
                    # Email subject *must not* contain newlines
					subject = ''.join(subject.splitlines())
					email = loader.render_to_string(email_template_name, c)
					send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                result = self.form_valid(form)
                messages.success(request, 'Email has been sent to ' + data +"'s email address. Please check its inbox to continue reseting password.")
                return result
            result = self.form_invalid(form)
            messages.error(request, 'This username does not exist in the system.')
            return result
            return self.form_invalid(form)