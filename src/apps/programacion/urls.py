from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^aula-listado/$', views.aula_listado, name='aula_listado'),
    url(r'^aula-crear/$', views.aula_crear_modificar, name='aula_crear'),
    url(r'^turno-listado/$', views.turno_listado, name='turno_listado'),
    url(r'^api-turno-agregar/$', views.api_turno_agregar, name='api_turno_agregar'),
    url(r'^api-turno-actualizar/$', views.api_turno_actualizar, name='api_turno_actualizar'),
]
