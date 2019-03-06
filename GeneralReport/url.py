from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import *
from .models import *

urlpatterns = [
    url(r'^pruebaa', Prueba.as_view(), name="prueba"),
    ]