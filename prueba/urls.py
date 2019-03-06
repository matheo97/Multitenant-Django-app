from django.conf.urls import url

from .views import prueba

urlpatterns = [
    url(r'^prueba$', prueba, name="prueba"),
]