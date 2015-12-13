from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.db import connection
from django.forms.models import modelformset_factory
from apps.common.util import paginador_general
from .models import Turno, Horario, Aula, Programacion, Periodo
from django.http import JsonResponse
import json
# Create your views here.


def turno_listado(request):
    turnos = Turno.objects.all().order_by('nombre')
    return render(request, 'programacion/turno_listado.html', locals())


def horario_listado(request):
    turnos = Turno.objects.all().order_by('nombre')
    horarios = Horario.objects.all().prefetch_related("turno")
    pagina = request.GET.get("pag", 1)
    pagina_cantidad = request.GET.get('pcantidad', 2)
    query_turno = request.GET.get("horario_seleccionar", False)
    if query_turno:
        horarios = horarios.filter(turno__pk=query_turno)
    horarios = paginador_general(horarios, pagina_cantidad, pagina)
    return render(request, 'programacion/horario_listado.html', locals())


def horario_crear_modificar(request, pk=False):
    turno = get_object_or_404(Turno, pk=pk)
    HorarioFormSet = modelformset_factory(Horario, extra=1, min_num=1, validate_min=True, can_delete=True, fields=('hora', 'hora_fin', 'id'))
    if request.method == "POST":
        horarioFormSet = HorarioFormSet(request.POST, queryset=Horario.objects.filter(turno__pk=pk))
        if horarioFormSet.is_valid():
            horarioFormSet.save()
            return redirect(reverse("programacion:horario_listado"))
    else:
        horarioFormSet = HorarioFormSet(queryset=Horario.objects.filter(turno__pk=pk))
    return render(request, 'programacion/horario_crear_modificar.html', locals())


def aula_listado(request):
    cursor = connection.cursor()
    aulas = cursor.execute("Select * From programacion_aula")

    return render(request, 'programacion/aula_listado.html', locals())


def programacion_listado(request):
    programacion = Programacion.objects.all().prefetch_related('periodo').prefetch_related('aula').prefetch_related('horario').prefetch_related('profesor').prefetch_related('ciclo_idioma')
    return render(request, 'programacion/programacion_listado.html', locals())


def aula_crear_modificar(request, pk=False):
    AulaFormSet = modelformset_factory(Aula, extra=1, min_num=1, validate_min=True, fields=('capacidad', 'numero_aula', 'id'))
    if request.method == "POST":
        aulaFormSet = AulaFormSet(request.POST, queryset=Aula.objects.all())
        print aulaFormSet
        if aulaFormSet.is_valid():
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
