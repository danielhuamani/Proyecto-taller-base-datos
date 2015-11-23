# -*- coding: utf-8 -*-
# SQL #
from django.db import connection
from logging import getLogger
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext as ctx

from .forms import (LoginForm,)
from .models import Usuario

log = getLogger('django')


def bienvenido(request):
    prueba = "texdasdsato"

    return render(request, 'sistema/bienvenido.html', locals())


# def registro(request):
#     log.info('VIEW: registro')

#     if request.user.is_authenticated():
#         return redirect(reverse('auth:logged_view'))

#     if request.method == 'POST':
#         form = RegistroForm(request.POST)

#         if form.is_valid():
#             form.save()
#             user = form.auth()
#             login(request, user)

#             return redirect(reverse('auth:logged_view'))
#         else:
#             log.warning('Error de formulario')
#     else:
#         form = RegistroForm()

#     return render('auth/registro.html', locals(),
#         context_instance=ctx(request))


def login_view(request):
    log.info('VIEW: login_view')
    # query_usuario = Usuario.objects.raw("Select * From sistema_usuario where id = %s", [1])
    # for query in query_usuario:
    #     print "--------------"
    #     print query.email
    #     print query.password
    # if request.user.is_authenticated():
    #     return redirect(reverse('sistema:logged_view'))
    # cursor = connection.cursor()
    # cursor.execute("Select * From sistema_usuario")
    # print cursor.fechone()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.auth()
            if user is not None:
                if user.is_active:
                    user.last_login = timezone.now()
                    user.save()
                    login(request, user)
                    return redirect(reverse('sistema:bienvenido'))
                else:
                    messages.add_message(request, messages.WARNING,
                        'El usuario no se encuentra activo')
            else:
                messages.add_message(request, messages.WARNING,
                        u'El email y contraseña son inválidos')
        else:
            log.warning('Error de formulario')
    else:
        form = LoginForm()

    return render(request, 'sistema/login.html', locals())


def salir(request):
    return logout_then_login(request, reverse('sistema:login_view'))


# def set_password(request, uuid_hash):
#     log.info('VIEW: set_password')

#     if request.method == 'POST':
#         form = SetPasswordForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form.enviaEmail()
#             return HttpResponseRedirect(
#                 reverse('auth:set_password_success'))
#         else:
#             log.warning('Error de formulario')
#     else:
#         try:
#             user = Usuario.objects.get(uuid_hash=uuid_hash)
#         except Usuario.DoesNotExist():
#             user = None
#         form = SetPasswordForm(initial={'email': user.email,
#             'uuid_hash': uuid_hash})

#     return render('auth/password/set-password.html', locals(),
#         context_instance=ctx(request))


# def set_password_success(request):
#     '''
#         Pantalla mostrada al cambiar la contraseña satisfactoriamente.
#         Redirecciona al Login y muestra un mensaje.
#     '''
#     log.info('VIEW: set_password_success')

#     return redirect(reverse('auth:login') + '?up=1')


# def recupera_password(request):
#     log.info('VIEW: recupera_passowrd')

#     if request.method == 'POST':
#         form = RecuperaPasswordForm(request.POST)
#         if form.is_valid():
#             form.enviaEmail()
#             messages.add_message(request, messages.INFO,
#                         'Se le ha enviado un email con las instrucciones a'
#                         ' seguir')
#         else:
#             log.warning('Error de formulario')
#     else:
#         form = RecuperaPasswordForm()

#     return render('auth/password/recupera-password.html', locals(),
#         context_instance=ctx(request))


# # PRIVATE VIEW
# @login_required(login_url=reverse_lazy('auth:login'))
# def logged_view(request):
#     log.info('VIEW: logged_view')

#     return render('auth/privado.html', locals(),
#         context_instance=ctx(request))
