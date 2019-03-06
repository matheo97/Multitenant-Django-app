from django.contrib import admin

from Usuario.models import *


admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Administrador)
admin.site.register(Digitador)