from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio_matricula, name='inicio_matricula'),
    url(r'^matricula/(?P<pk>\d+)/$', views.matricular, name='matricular'),
    # url(r'^periodo_matricula/$', views.periodo_matricula, name='periodo_matricula'),
    url(r'^matricula-gracias/$', views.matricula_gracias, name='matricula_gracias'),
    url(r'^mi-matricula-listado/$', views.mi_matricula_listado, name='mi_matricula_listado'),
    url(r'^matricula-detalle/(?P<pk>\d+)/$', views.periodo_matricula_detalle, name='periodo_matricula_detalle'),
    url(r'^matricula-alumno-detalle/(?P<pk>\d+)/$', views.matricula_alumno_detalle, name='matricula_alumno_detalle'),
    url(r'^matricula-valida/(?P<pk>\d+)/$', views.matricula_valida, name='matricula_valida'),
    url(r'^api-validar-matricula/$', views.api_validar_matricula, name='api_validar_matricula'),
    url(r'^matricula-pdf/(?P<pk>\d+)/$', views.matricula_generar_pdf, name='matricula_generar_pdf'),
]
