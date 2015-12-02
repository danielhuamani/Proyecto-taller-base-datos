from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db import connection
from django.forms.models import modelformset_factory
from .models import Turno, Horario, Aula
from django.http import JsonResponse
import json
# Create your views here.


def turno_listado(request):
    turnos = Turno.objects.all().order_by('nombre')
    return render(request, 'programacion/turno_listado.html', locals())


def aula_listado(request):
    cursor = connection.cursor()
    aulas = cursor.execute("Select * From programacion_aula")

    return render(request, 'programacion/aula_listado.html', locals())


def aula_crear_modificar(request, pk=False):
    AulaFormSet = modelformset_factory(Aula, extra=1, min_num=1, validate_min=True, fields=('capacidad', 'numero_aula', 'id'))
    if request.method == "POST":
        aulaFormSet = AulaFormSet(request.POST, queryset=Aula.objects.all())
        print aulaFormSet
        if aulaFormSet.is_valid():
            print "entro"
            aulaFormSet.save()
            return redirect(reverse("programacion:aula_listado"))
    else:
        aulaFormSet = AulaFormSet(queryset=Aula.objects.all())
    return render(request, 'programacion/aula_crear_modificar.html', locals())


def api_turno_agregar(request):

    if request.is_ajax():
        if request.method == "POST":
            listado_turno = []
            print request.POST.get("Turno")
            for turno in json.loads(request.POST.get("turno")):
                if turno:
                    guardado_turno = Turno(nombre=turno)
                #     if idioma:
                #         listado_turno.append(Idioma(nombre=idioma))
                # guardado_turno = Idioma.objecdots.bulk_create(listado_turno)
                    guardado_turno.save()
                    listado = {}
                    listado['nombre'] = guardado_turno.nombre
                    listado['id'] = guardado_turno.id
                    listado_turno.append(listado)
            data = {
                'listado': listado_turno,
            }
    else:
        data = {"status": "error"}
    return JsonResponse(data)


def api_turno_actualizar(request):

    if request.is_ajax():
        if request.method == "POST":
            guardar_turno = Turno.objects.get(id=request.POST.get("turno_pk"))
            guardar_turno.nombre = request.POST.get("turno_nombre")
            guardar_turno.save()
            data = {'status': 'ok'}
    else:
        data = {"status": "error"}
    return JsonResponse(data)
