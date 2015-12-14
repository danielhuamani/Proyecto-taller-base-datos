from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^aula-listado/$', views.aula_listado, name='aula_listado'),
    url(r'^aula-crear/$', views.aula_crear_modificar, name='aula_crear'),
    url(r'^turno-listado/$', views.turno_listado, name='turno_listado'),
    url(r'^horario-listado/$', views.horario_listado, name='horario_listado'),
    url(r'^horario-agregar/(?P<pk>\d+)/$', views.horario_crear_modificar, name='horario_crear'),
    url(r'^periodo-listado/$', views.periodo_listado, name='periodo_listado'),
    url(r'^programacion-listado/(?P<pk>\d+)/$', views.programacion_listado, name='programacion_listado'),
    url(r'^programacion-agregar/(?P<pk_periodo>\d+)/(?P<pk_idioma>\d+)/$', views.programacion_crear_modificar, name='programacion_crear_modificar'),
    url(r'^api-turno-agregar/$', views.api_turno_agregar, name='api_turno_agregar'),
    url(r'^api-turno-actualizar/$', views.api_turno_actualizar, name='api_turno_actualizar'),
]
