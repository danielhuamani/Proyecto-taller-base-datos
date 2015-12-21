
# -*- coding: utf-8 -*-
from logging import getLogger

from django import forms
from django.contrib.auth import authenticate
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import get_template
from django.conf import settings

from .models import Usuario

log = getLogger('django')


class LoginForm(forms.Form):
    ''' Formulario de acceso al sistema '''
    username = forms.EmailField(label='Email')
    username.widget.attrs.update({'autofocus': 'true', 'tabindex': '1'})
    password = forms.CharField(label='Contraseña', min_length=6,
        max_length=32, widget=forms.PasswordInput)
    password.widget.attrs.update({'tabindex': '2'})

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     try:
    #         Usuario.objects.get(email=username)
    #     except Usuario.DoesNotExist:
    #         mensaje = u'El email no ha sido registrado'
    #         raise forms.ValidationError(mensaje)

    #     return username

    def auth(self):
        cd = self.cleaned_data
        return authenticate(username=cd['username'], password=cd['password'])


class RegistroForm(forms.Form):
    ''' Formulario de Registro '''
    username = forms.EmailField(label='Email')
    password = forms.CharField(label='Contraseña', min_length=7,
        max_length=32, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            Usuario.objects.get(email=username)
            mensaje = (u'El email ya ha sido registrado. <br>Puede ingresar' +
                u'desde <a class="ingresar" href={0}>aquí</a>'.format(
                    reverse('auth:login')))
            raise forms.ValidationError(mensaje)
        except Usuario.DoesNotExist:
            return username

    def save(self):
        cd = self.cleaned_data
        Usuario(email=cd['username'], password=cd['password']).save()

    def auth(self):
        cd = self.cleaned_data
        return authenticate(username=cd['username'], password=cd['password'])


class RecuperaPasswordForm(forms.Form):
    '''
        Formulario que solicita el email para iniciar el proceso de
        recuperación de contraseña.
    '''
    username = forms.EmailField(label='Email')

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            self.u = Usuario.objects.get(email=username)
        except Usuario.DoesNotExist:
            mensaje = 'El email no ha sido registrado'
            raise forms.ValidationError(mensaje)

        return username

    def enviaEmail(self):
        htmly = get_template('auth/password/email-setpassword.html')
        site = Site.objects.get(id=settings.SITE_ID)
        cd = self.cleaned_data
        cd['SITE'] = site.domain
        cd['STATIC_URL'] = site.domain + '/' + settings.STATIC_URL
        cd['usuario'] = self.u
        d = Context(cd)

        html_content = htmly.render(d)
        asunto = u'Actualización de Contraseña'
        mail = '{0}<{1}>'.format(settings.PROJECT_NAME,
            settings.DEFAULT_FROM_EMAIL)
        msg = EmailMessage(asunto, html_content, mail, [self.u.email])
        msg.content_subtype = "html"
        msg.send()


class SetPasswordForm(forms.Form):
    uuid_hash = forms.CharField(label='', widget=forms.HiddenInput)
    email = forms.EmailField(label='Email')
    email.widget.attrs.update({'readonly': 'readonly'})
    password = forms.CharField(label='Nueva contraseña', min_length=7,
        max_length=32, widget=forms.PasswordInput)

    def clean_email(self):
        uuid_hash = self.cleaned_data['uuid_hash']
        email = self.cleaned_data['email']
        try:
            self.u = Usuario.objects.get(email=email, uuid_hash=uuid_hash)
        except Usuario.DoesNotExist:
            raise forms.ValidationError('El email o la clave temporal son' +
                'incorrectos!')

        return email

    def save(self):
        cd = self.cleaned_data
        usuario = self.u
        usuario.set_password = False
        usuario.uuid_hash = ''
        usuario.password = cd['password']
        usuario.save()

    def enviaEmail(self):
        htmly = get_template('auth/password/email-password-update.html')
        site = Site.objects.get(id=settings.SITE_ID)
        cd = self.cleaned_data
        cd['SITE'] = site.domain
        cd['STATIC_URL'] = site.domain + '/' + settings.STATIC_URL
        cd['usuario'] = self.u
        d = Context(cd)

        html_content = htmly.render(d)
        asunto = u'Actualización de Contraseña'
        mail = '{0}<{1}>'.format(settings.PROJECT_NAME,
            settings.DEFAULT_FROM_EMAIL)
        msg = EmailMessage(asunto, html_content, mail, [self.u.email])
        msg.content_subtype = "html"
        msg.send()
