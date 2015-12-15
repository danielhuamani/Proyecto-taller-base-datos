from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from .forms import ProfesorForm
from apps.programacion.models import Periodo
from apps.common.util import paginador_general
from .models import Profesor
# Create your views here.


def profesor_listado(request):
    profesores = Profesor.objects.all()
    pagina = request.GET.get("pag", 1)
    pagina_cantidad = request.GET.get('pcantidad', 2)
    if request.GET.get("buscar"):
        buscar = request.GET.get("buscar")
        profesores = profesores.filter(Q(email__icontains=buscar) | Q(nombres__icontains=buscar) | Q(apellidos__icontains=buscar) | Q(codigo_profesor__icontains=buscar))
    profesores = paginador_general(profesores, pagina_cantidad, pagina)
    return render(request, "profesor/profesor_listado.html", locals())


def profesor_crear_modificar(request, pk=False):
    if pk:
        profesor = get_object_or_404(Profesor, pk=pk)
    else:
        profesor = Profesor()

    if request.method == "POST":
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect(reverse("alumno_profesor:profesor_listado"))
    else:
        form = ProfesorForm(instance=profesor)

    return render(request, "profesor/profesor_crear_modificar.html", locals())
