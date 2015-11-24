from django.shortcuts import render
from .models import Idioma
from .forms import IdiomaForm
from django.forms import formset_factory
from django.db import connection
from django.http import JsonResponse
import json
# Create your views here.


def idioma_listado(request):
    idiomas = Idioma.objects.all().order_by("nombre")
    # cursor = connection.cursor()
    # cursor.execute("Select * From idioma_idioma")
    # for nue in idiomas:
    #     print nue
    return render(request, "idioma/idioma_listado.html", locals())


def idioma_nivel_listado(request):
    return render(request, "idioma/idioma_nivel_listado.html", locals())


def api_idioma_agregar(request):

    if request.is_ajax():
        if request.method == "POST":
            listado_idioma = []
            for idioma in json.loads(request.POST.get("idioma")):
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
