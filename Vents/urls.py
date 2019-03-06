from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import *
from .models import *
from django.contrib.auth import views


urlpatterns = [
    url(r'^venta/$', Ventas.as_view() , name = "venta"),
    url(r'^ventaRegistrada/$', RegistrarVenta.as_view() , name = "ventaRegistrada"),
    
]