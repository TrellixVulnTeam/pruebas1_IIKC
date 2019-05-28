from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from usuario.models import Usuario
from jvc.forms import InicioSesionForm
from django.contrib.auth.views import LoginView


def home(request):
    return render(request, 'jvc/inicioSesion.html')


def dashboard(request):
    return render(request, 'jvc/dashboard.html')


def inicioSesion(request):
    if request.method == "POST":
        form = InicioSesionForm(request.POST)
        if form.is_valid():
            try:
                usuarioFormulario = form.clean_data['usuario']
                claveFormulario = form.clean_data['clave']
                usuarioBD = Usuario.objects.get(usuario=usuarioFormulario)
                if usuarioBD.usuario == usuarioFormulario and usuarioBD.clave == claveFormulario:
                    return redirect('/dashboard/')
                else:
                    return HttpResponseRedirect('')
            except:
                pass
        else:
            return HttpResponseRedirect('')
    else:
        form = InicioSesionForm()
    return render(request, 'jvc/inicioSesion.html', {'form': form})

