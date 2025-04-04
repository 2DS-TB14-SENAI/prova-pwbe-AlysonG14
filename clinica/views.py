from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from .form import ClinicaForm

# Create your views here.

def base(request):
    return render(request, 'clinica/base.html')

def listar_medicos(request):
    lista_medico = Médico.objects.all()
    return render(request, 'clinica/listar_medicos.html', {"lista_medico" : lista_medico})

def detalhes_consulta(request):
    consulta = Consulta.objects.all()
    return render (request, 'clinica/exibir_consulta.html', {'consulta': consulta})

def criar_consulta(request):
    if request.method == 'POST':
        form = ClinicaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listar_medicos.html')
    else:
         form = ClinicaForm()
    return render(request, 'clinica/form_consulta.html', {"form": form})


def detalhe_consulta(request, pk):
        paciente = Consulta.objects.get(pk=pk)
        return render(request, 'clinica/exibir_consulta.html', {"paciente" : paciente})



