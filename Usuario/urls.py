from django.conf.urls import url, include
from .views import *
from .models import *
from .forms import *
from django.contrib.auth import views
from django.contrib import admin
from .facebook import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^actualizar_lista_usuarios$', actualizar_lista_usuarios, name="actualizar_lista_usuarios"),
 	url(r'^ingresar', loginIn, name="iniciar_sesion"),
    url(r'^salir$', views.logout, {'next_page': 'usuario:iniciar_sesion'}, name="cerrar_sesion"),
    url(r'^crear-administrador$', CrearUsuarioAdministrador.as_view(), name="crear_administrador"),
    url(r'^crear-cliente$', CrearUsuarioCliente.as_view(), name="crear_cliente"),
    url(r'^crear-digitador$', CrearUsuarioDigitador.as_view(), name="crear_digitador"),
    url(r'^listar$', listar_usuario_view, name="listar_usuario"),
    #url(r'^register$', register_form, name="register"),
    
    url(r'^visualizar-usuario/(?P<id_usuario>\d+)$', visualizar_usuario_view, {'modelo': Usuario}, name="perfil_usuario"),
    
    url(r'^modificar-administrador/(?P<id_usuario>\d+)$', ModificarUsuario.as_view(), {'modelo': 'Administrador'}, name="modificar_administrador"),
    url(r'^modificar-digitador/(?P<id_usuario>\d+)$', ModificarUsuario.as_view(), {'modelo': 'Digitador'}, name="modificar_digitador"),
    url(r'^modificar-cliente/(?P<id_usuario>\d+)$', ModificarUsuario.as_view(), {'modelo': 'Cliente'}, name="modificar_cliente"),
    
    url(r'^eliminar/(?P<id_usuario>\d+)$', eliminar_usuario_view, {'modelo':Usuario}, name="eliminar_usuario"),
    url(r'^desactivar$', DesactivarCliente.as_view(),  name="desactivar_usuario"),
    url(r'^activar$', ActivarCliente.as_view(),  name="activar_usuario"),
    url(r'^activar/(?P<id_usuario>\d+)$', activar_usuario_view, {'modelo':Usuario}, name="activar_usuario"), 
    url(r'^permisos$', configurar_permisos_view, name="configurar_permisos"),
    url(r'^killcliente$', killCliente, name="kill_cliente"),
]

