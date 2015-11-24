from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^aula-listado/$', views.aula_listado, name='aula_listado'),
    url(r'^aula-crear/$', views.aula_crear_modificar, name='aula_crear'),
]
