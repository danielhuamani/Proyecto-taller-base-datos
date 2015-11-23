from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^ingresar/$', views.login_view, name='login_view'),
    url(r'^bienvenido/$', views.bienvenido, name='bienvenido'),
    url(r'^salir/$', views.salir, name='salir'),
    # url(r'^registro/$', 'registro', name='registro'),

    # # RECUPERAR PASSWORD
    # url(r'^recuperar-password/$', 'recupera_password', name='recupera_password'),
    # url(r'^cambiar-password/(?P<uuid_hash>[-\w]+)$', 'set_password', name='set_password'),
    # url(r'^cambiar-password-ok/$', 'set_password_success', name='set_password_success'),

    # # PRIVATE VIEWS
    # url(r'^auth/$', 'logged_view', name='logged_view')
    # url(r'^login/$', 'home_prueba', name='ingresar'),
]
