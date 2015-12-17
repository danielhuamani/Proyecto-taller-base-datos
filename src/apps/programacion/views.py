from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.db import connection
from django.forms.models import modelformset_factory
from apps.common.util import paginador_general
from apps.idioma.models import Idioma, CicloIdioma
from apps.alumno_profesor.models import Profesor
from .models import Turno, Horario, Aula, Programacion, Periodo
from django.http import JsonResponse
from .forms import PeriodoForm, ProgramacionForm
import json
import datetime
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
    HorarioFormSet = modelformset_factory(Horario, extra=0, min_num=1, validate_min=True, can_delete=True, fields=('hora', 'hora_fin', 'id', 'turno'))
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


def periodo_listado(request):
    periodos = Periodo.objects.all().order_by("-fecha_final")
    pagina = request.GET.get("pag", 1)
    pagina_cantidad = request.GET.get('pcantidad', 50)
    query_fecha_inicio = request.GET.get("fecha_inicio", "")
    query_fecha_final = request.GET.get("fecha_final", "")
    if query_fecha_inicio:
        query_fecha_inicio = datetime.datetime.strptime(query_fecha_inicio, "%d-%m-%Y").date()
        periodos = periodos.filter(fecha_inicio__gte=query_fecha_inicio)
    if query_fecha_final:
        query_fecha_final = datetime.datetime.strptime(query_fecha_final, "%d-%m-%Y").date()
        periodos = periodos.filter(fecha_inicio__lte=query_fecha_final)
    if request.method == "POST":
        fecha_inicio = request.POST.get("form_fecha_inicio")
        fecha_final = request.POST.get("form_fecha_final")
        fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d-%m-%Y").date()
        fecha_final = datetime.datetime.strptime(fecha_final, "%d-%m-%Y").date()
        Periodo(fecha_final=fecha_final, fecha_inicio=fecha_inicio).save()
        return redirect(reverse("programacion:periodo_listado"))
    else:
        ejecuto_post = False
    periodos = paginador_general(periodos, pagina_cantidad, pagina)
    return render(request, 'programacion/periodo_listado.html', locals())


def programacion_listado(request, pk=False):
    periodo = get_object_or_404(Periodo, pk=pk)
    idiomas = Idioma.objects.all()
    programacion = Programacion.objects.filter(periodo=periodo).prefetch_related('aula').prefetch_related('horario__turno').prefetch_related('profesor').prefetch_related('ciclo_idioma__idioma').prefetch_related('ciclo_idioma__nivel_idioma')
    pagina = request.GET.get("pag", 1)
    pagina_cantidad = request.GET.get('pcantidad', 25)
    query_idioma = request.GET.get("query_idioma", False)
    if query_idioma:
        programacion = programacion.filter(ciclo_idioma__idioma=query_idioma)
    programacion = paginador_general(programacion, pagina_cantidad, pagina)
    return render(request, 'programacion/programacion_listado.html', locals())


def programacion_crear_modificar(request, pk_idioma=False, pk_periodo=False):
    periodo = get_object_or_404(Periodo, pk=pk_periodo)
    aulas = Aula.objects.all()
    profesores = Profesor.objects.all()
    horarios = Horario.objects.all()
    ciclo_idiomas = CicloIdioma.objects.filter(idioma=pk_idioma)
    if request.method == "POST":
        form = ProgramacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("programacion:programacion_listado", kwargs={'pk': pk_periodo}))
    else:
        form = ProgramacionForm()
    return render(request, 'programacion/programacion_crear_modificar.html', locals())


def aula_crear_modificar(request, pk_idioma=False):
    AulaFormSet = modelformset_factory(Aula, extra=1, min_num=1, validate_min=True, fields=('capacidad', 'numero_aula', 'id'))
    if request.method == "POST":
        aulaFormSet = AulaFormSet(request.POST, queryset=Aula.objects.all())
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
