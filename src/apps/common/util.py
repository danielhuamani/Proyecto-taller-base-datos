from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginador_general(listado, cantidad_paginar=25, pagina=1):
    listado = listado
    paginator = Paginator(listado, cantidad_paginar)
    page = pagina
    try:
        listado = paginator.page(page)
    except PageNotAnInteger:
        listado = paginator.page(1)
    except EmptyPage:
        listado = paginator.page(paginator.num_pages)
    return listado
