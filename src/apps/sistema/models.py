# -*- coding: utf-8 -*-

from pbkdf2 import crypt
from logging import getLogger
from uuid import uuid4
import re

from django.conf import settings
from django.db import models

log = getLogger('django')

SECRET_KEY = settings.AUTH_SECRET_KEY
SALT = ''.join(re.findall("[a-zA-Z0-9]+", SECRET_KEY))
NUMERO_DE_ITERACIONES = 500


class Usuario(models.Model):
    is_active = models.BooleanField('¿Activo?', default=True, blank=True)
    last_login = models.DateTimeField('Último Login', blank=True, null=True)
    email = models.EmailField('Email', blank=True)
    password = models.CharField('Contraseña', max_length=255, default='',
        blank=True)

    set_password = models.BooleanField('¿Contraseña encriptada?', default=False)
    uuid_hash = models.CharField('UUID', max_length=36, default='', blank=True,
        help_text='Aleautorio utilizado para recuperar la contraseña')

    def __unicode__(self):
        return unicode(self.password)

    class Meta:
        verbose_name = u'Administrador Usuario'
        verbose_name_plural = u'Administrador Usuarios'

    def save(self, *args, **kwargs):
        if not self.uuid_hash:
            self.uuid_hash = str(uuid4())

        if not self.set_password:
            self.password = encrypt_password(self.password)
            self.set_password = True

        super(Usuario, self).save(*args, **kwargs)

    def is_password_valid(self, password):
        return is_password_valid(password, self.password)

    def is_authenticated(self):
        return True

    @property
    def is_staff(self):
        return False


# HELPERS
def encrypt_password(password):
    ''' Encripta la contraseña '''
    return crypt(password, SALT, NUMERO_DE_ITERACIONES)


def is_password_valid(password, encoded):
    ''' Contrasta la contraseña brindada con el valor encriptado '''
    return encrypt_password(password) == encoded
