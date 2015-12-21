from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profesor-listado/$', views.profesor_listado, name='profesor_listado'),
    url(r'^profesor-crear/$', views.profesor_crear_modificar, name='profesor_crear'),
    url(r'^profesor-modificar/(?P<pk>\d+)/$', views.profesor_crear_modificar, name='profesor_modificar'),
    url(r'^alumno-listado/$', views.alumno_listado, name='alumno_listado'),
    url(r'^alumno-registrar/$', views.alumno_crear_modificar, name='alumno_crear'),
]
