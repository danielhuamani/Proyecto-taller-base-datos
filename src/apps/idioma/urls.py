from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^idioma-listado/$', views.idioma_listado, name='idioma_listado'),
    url(r'^idioma-nivel-listado/$', views.idioma_nivel_listado, name='idioma_nivel_listado'),
    url(r'^idioma-ciclo-listado/$', views.idioma_ciclo_listado, name='idioma_ciclo_listado'),
    url(r'^idioma-ciclo-agregar/(?P<pk_idioma>\d+)/(?P<pk_nivel>\d+)/$', views.idioma_ciclo_crear, name='idioma_ciclo_crear'),
    url(r'^api-idioma-agregar/$', views.api_idioma_agregar, name='api_idioma_agregar'),
    url(r'^api-idioma-actualizar/$', views.api_idioma_actualizar, name='api_idioma_actualizar'),
    url(r'^api-nivel-idioma-agregar/$', views.api_nivel_idioma_agregar, name='api_nivel_idioma_agregar'),
    url(r'^api-nivel-idioma-actualizar/$', views.api_nivel_idioma_actualizar, name='api_nivel_idioma_actualizar'),
    # url(r'^registro/$', 'registro', name='registro'),

    # # RECUPERAR PASSWORD
    # url(r'^recuperar-password/$', 'recupera_password', name='recupera_password'),
    # url(r'^cambiar-password/(?P<uuid_hash>[-\w]+)$', 'set_password', name='set_password'),
    # url(r'^cambiar-password-ok/$', 'set_password_success', name='set_password_success'),

    # # PRIVATE VIEWS
    # url(r'^auth/$', 'logged_view', name='logged_view')
    # url(r'^login/$', 'home_prueba', name='ingresar'),
]
