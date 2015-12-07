# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # WEB
    url(r'^sistema/', include('apps.sistema.urls', namespace="sistema")),
    url(r'^idioma/', include('apps.idioma.urls', namespace="idioma")),
    url(r'^programacion/', include('apps.programacion.urls', namespace="programacion")),
    url(r'', include('apps.alumno_profesor.urls', namespace="alumno_profesor")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'apps.web.views.page_404'
handler500 = 'apps.web.views.page_500'
