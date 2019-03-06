from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import *
from .models import *
from django.contrib.auth import views


urlpatterns = [
    url(r'^nuevo_producto', CrearProducto.as_view(), name="nuevoProducto"),
    url(r'^nuevo_topping', CrearTopping.as_view(), name="nuevoTopping"),
    url(r'^algo', algo, name='algo'),
    url(r'^listar_producto/$', ListarProducto.as_view() , name = "listarProducto"),
    url(r'^listar_topping/$', ListarTopping.as_view() , name = "listartopping"),
    url(r'^editar_topping/(\d+)/$', EditarToppig.as_view() , name = 'editarTopping'),
    url(r'^editar_producto/(\d+)/$', EditarProducto.as_view() , name = 'editarProducto'),
    
    ]