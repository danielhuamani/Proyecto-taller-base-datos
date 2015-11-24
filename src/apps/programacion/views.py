from django.shortcuts import render
from django.db import connection
# Create your views here.


def aula_listado(request):
    cursor = connection.cursor()
    aulas = cursor.execute("Select * From programacion_aula")

    return render(request, 'programacion/aula_listado.html', locals())


def aula_crear_modificar(request, pk=False):
    return render(request, 'programacion/aula_crear_modificar.html', locals())
