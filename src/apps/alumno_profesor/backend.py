# -*- coding: utf-8 -*-

from datetime import datetime
from logging import getLogger

from .models import Alumno

log = getLogger('django')


class AuthBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user = Alumno.objects.get(email=username)
        except Alumno.DoesNotExist:
            log.debug(u'El email no es válido')
            return None

        if user.contrasena == password:
            user.last_login = datetime.now()
            user.save()
            return user

        log.debug(u'La contraseña es incorrecta')
        return None

    def get_user(self, username):
        log.debug('get_user: {0}'.format(username))
        try:
            return Alumno.objects.get(id=username)
        except Alumno.DoesNotExist:
            log.debug('El usuario no existe')
            return None
