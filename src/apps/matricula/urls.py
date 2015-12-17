from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio_matricula, name='inicio_matricula'),
    url(r'^matricula/(?P<pk>\d+)/$', views.matricular, name='matricular'),
    url(r'^periodo_matricula/$', views.periodo_matricula, name='periodo_matricula'),
    url(r'^matricula-detalle/(?P<pk>\d+)/$', views.periodo_matricula_detalle, name='periodo_matricula_detalle'),
    url(r'^matricula-gracias/$', views.matricula_gracias, name='matricula_gracias'),
]
