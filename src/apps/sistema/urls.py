from django.conf.urls import patterns, url


urlpatterns = patterns('apps.sistema.views',
    url(r'^ingresar/$', 'login_view', name='login_view'),
    # url(r'^salir/$', 'logout', name='logout'),
    # url(r'^registro/$', 'registro', name='registro'),

    # # RECUPERAR PASSWORD
    # url(r'^recuperar-password/$', 'recupera_password', name='recupera_password'),
    # url(r'^cambiar-password/(?P<uuid_hash>[-\w]+)$', 'set_password', name='set_password'),
    # url(r'^cambiar-password-ok/$', 'set_password_success', name='set_password_success'),

    # # PRIVATE VIEWS
    # url(r'^auth/$', 'logged_view', name='logged_view')
    # url(r'^login/$', 'home_prueba', name='ingresar'),
)
