from .models import Franquicia
from django.db import connection

# def obtener_todos_mensajes():
#     mensajes = []
#     tenants = Franquicia.objects.exclude(schema_name='public')
#     for tenant in tenants:
#         connection.set_tenant(tenant)
#         mensajes_tenant_actual = {
#             'nombre_tenant': tenant.nombre_tenant,
#             'mensajes_tenant': [mensaje.cuerpo_mensaje for mensaje in Mensaje.objects.all()]
#         }
#         mensajes.append(mensajes_tenant_actual)
#     connection.set_schema_to_public()
#     return mensajes
