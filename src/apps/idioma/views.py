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
        data = {"status": "ok"}
        if request.method == "POST":
            listado_idioma = []
            for idioma in json.loads(request.POST.get("idioma")):
                if idioma:
                    listado_idioma.append(Idioma(nombre=idioma))
            Idioma.objects.bulk_create(listado_idioma)
    else:
        data = {"status": "error no ajax"}
    return JsonResponse(data)
