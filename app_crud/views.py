from django.db.models.fields import DateField
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.conf import path
from django.utils.regex_helper import contains
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import datetime

from .models import Crud


# Create your views here.


def mostrarTemplate(request):
    crud = Crud.objects.all().order_by('-created_at')

    return render(request, 'app_crud/mostrar_template.html', {'cruds': crud})


@csrf_exempt
def criarElemento(request):
    if(request.POST['crud'].strip() != ''):

        conteudo = (request.POST['crud'])
        Crud.objects.create(nome=conteudo, done='doing')

    return redirect('/')


def mudarStatus(request, id):
    crud = get_object_or_404(Crud, pk=id)

    if(crud.done == 'doing'):
        crud.done = 'done'
    else:
        crud.done = 'doing'

    crud.save()
    return redirect('/')


def deletarElemento(request, id):
    crud = get_object_or_404(Crud, pk=id)

    crud.delete()
    return redirect('/')


def editarElemento(request, id):
    if request.method == 'POST':
        valor = request.POST.get('editCrud')
        if valor.strip() != '':
            
            crud = get_object_or_404(Crud, pk=id)
            crud.nome=valor
            crud.update_at=datetime.datetime.now()
            crud.save()
            
    return redirect('/')


def pegarValores(request, id):
    crud = Crud.objects.filter(id=id).values()
    return JsonResponse({"crud": list(crud)})
