from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from app.models import Televisores, Celulares, Notebooks

def mostrar_televisores(request):

    televisores = Televisores.objects.all()
    context = {'productos': televisores, 'categoria': 'televisores'}
    

    return render(request, 'mostrar.html', context=context)


def mostrar_celulares(request):

    celulares = Celulares.objects.all()
    context = {'productos': celulares, 'categoria': 'celulares'}

    return render(request, 'mostrar.html', context=context)

def mostrar_notebooks(request):

    notebooks = Notebooks.objects.all()
    context = {'productos': notebooks, 'categoria': 'notebooks'}

    return render(request, 'mostrar.html', context=context)


def mostrar_detalles(request, categoria, id):
    if categoria == 'televisores':
        producto = get_object_or_404(Televisores, pk=id)

    elif categoria == 'celulares':
        producto = get_object_or_404(Celulares, pk=id)

    elif categoria == 'notebooks':
        producto = get_object_or_404(Notebooks, pk=id)

    context = {'producto': producto}

    return render(request, 'details.html', context=context)

