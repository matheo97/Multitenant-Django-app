from django.conf.urls import url
from django.core.urlresolvers import reverse
from .views import *
from .models import *
from django.contrib.auth import views



urlpatterns = [
    url(r'^ventas-mes/$',  ventas_mes , name = "ventas_mes"),
    url(r'^registros-mes/$',  registrados_mes , name = "registrados_mes"),
    url(r'^pizzas-mas-vendidas/$',  pizzas_mas_vendidas , name = "pizzas_mas_vendidas"),
    url(r'^toppings-mas-vendidas/$',  toppings_mas_vendidos , name = "toppings_mas_vendidas"),
    url(r'^toppings-menos-vendidas/$',  toppings_menos_vendidos , name = "toppings_menos_vendidas"),
    url(r'^dias-mas-ventas/$',  dias_mas_ventas , name = "dias_mas_ventas"),
    
]