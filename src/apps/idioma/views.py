from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from .models import Idioma, NivelIdioma, CicloIdioma
from django.forms.models import modelformset_factory
from apps.common.util import paginador_general
from django.db import connection
from django.http import JsonResponse
import json
# Create your views here.


def idioma_listado(request):
    idiomas = Idioma.objects.all().order_by("nombre")
    # cursor = connection.cursor()
    # cursor.execute("Select * From idioma_idioma")
    # for nue in cursor:
    #     print nue
    return render(request, "idioma/idioma_listado.html", locals())


def idioma_nivel_listado(request):
    nivel_idiomas = NivelIdioma.objects.all().order_by("nombre")
    return render(request, "idioma/idioma_nivel_listado.html", locals())


def idioma_ciclo_listado(request):
    query_idioma = request.GET.get("idioma_seleccionar")
    query_nivel = request.GET.get("nivel_seleccionar")
    ciclo_idiomas = CicloIdioma.objects.all().prefetch_related("idioma").prefetch_related("nivel_idioma").order_by("idioma__nombre")
    pagina = request.GET.get("pag", 1)
    pagina_cantidad = request.GET.get('pcantidad', 2)
    if query_idioma:
        ciclo_idiomas = ciclo_idiomas.filter(idioma=query_idioma)
    if query_nivel:
        ciclo_idiomas = ciclo_idiomas.filter(nivel_idioma=query_nivel)
    nivel_idiomas = NivelIdioma.objects.all().order_by("nombre")
    idiomas = Idioma.objects.all().order_by("nombre")
    ciclo_idiomas = paginador_general(ciclo_idiomas, pagina_cantidad, pagina)
    return render(request, 'idioma/idioma_ciclo_listado.html', locals())


def idioma_ciclo_crear(request, pk_idioma=False, pk_nivel=False):
    idioma = get_object_or_404(Idioma, pk=pk_idioma)
    nivel = get_object_or_404(NivelIdioma, pk=pk_nivel)
    nivel_idiomas = NivelIdioma.objects.all().order_by("nombre")
    NivelFormSet = modelformset_factory(CicloIdioma, extra=0, min_num=1, validate_min=True, can_delete=True, fields=('nombre', 'idioma', 'nivel_idioma', 'id'))
    if request.method == "POST":
        nivelFormSet = NivelFormSet(request.POST, queryset=CicloIdioma.objects.filter(nivel_idioma=pk_nivel, idioma=pk_idioma))
        if nivelFormSet.is_valid():
            nivelFormSet.save()
            return redirect(reverse("idioma:idioma_ciclo_listado"))
    else:
        nivelFormSet = NivelFormSet(queryset=CicloIdioma.objects.filter(nivel_idioma=pk_nivel, idioma=pk_idioma))
    return render(request, 'idioma/idioma_ciclo_crear.html', locals())


def api_idioma_agregar(request):

    if request.is_ajax():
        if request.method == "POST":
            listado_idioma = []
            for idioma in json.loads(request.POST.get("idioma")):
                if idioma:
                    guardado_idioma = Idioma(nombre=idioma)
                #     if idioma:
                #         listado_idioma.append(Idioma(nombre=idioma))
                # guardado_idioma = Idioma.objecdots.bulk_create(listado_idioma)
                    guardado_idioma.save()
                    listado = {}
                    listado['nombre'] = guardado_idioma.nombre
                    listado['id'] = guardado_idioma.id
                    listado_idioma.append(listado)
            data = {
                'listado': listado_idioma,
            }
    else:
        data = {"status": "error"}
    return JsonResponse(data)


def api_idioma_actualizar(request):

    if request.is_ajax():
        if request.method == "POST":
            guardado_idioma = Idioma.objects.get(id=request.POST.get("idioma_pk"))
            guardado_idioma.nombre = request.POST.get("idioma_nombre")
            guardado_idioma.save()
            data = {'status': 'ok'}
    else:
        data = {"status": "error"}
    return JsonResponse(data)


def api_nivel_idioma_agregar(request):

    if request.is_ajax():
        if request.method == "POST":
            listado_idioma = []
            for idioma in json.loads(request.POST.get("idioma")):
                guardado_nivel_idioma = NivelIdioma(nombre=idioma)
            #     if idioma:
            #         listado_idioma.append(Idioma(nombre=idioma))
            # guardado_nivel_idioma = Idioma.objecdots.bulk_create(listado_idioma)
                guardado_nivel_idioma.save()
                listado = {}
                listado['nombre'] = guardado_nivel_idioma.nombre
                listado['id'] = guardado_nivel_idioma.id
                listado_idioma.append(listado)
            data = {
                'listado': listado_idioma,
            }
    else:
        data = {"status": "error"}
    return JsonResponse(data)


def api_nivel_idioma_actualizar(request):

    if request.is_ajax():
        if request.method == "POST":
            guardado_nivel_idioma = NivelIdioma.objects.get(id=request.POST.get("idioma_pk"))
            guardado_nivel_idioma.nombre = request.POST.get("idioma_nombre")
            guardado_nivel_idioma.save()
            data = {'status': 'ok'}
    else:
        data = {"status": "error"}
    return JsonResponse(data)
