from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio_matricula, name='inicio_matricula'),
    url(r'^matricula/(?P<pk>\d+)/$', views.matricular, name='matricular'),
]