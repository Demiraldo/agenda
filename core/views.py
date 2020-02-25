# primeira forma de redirecionar o index para uma outra view
# from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# primeira forma para redirecionar o index para outra view
# def index(request):
#    return redirect('/agenda/')

def logar_usuario(request):
    return render(request, 'login.html')


def logout_usuario(request):
    logout(request)
    return redirect('/')


def submit_usuario(request):
    if request.POST:
        nome_us = request.POST.get('usuario')
        senha_us = request.POST.get('senha')
        usuario = authenticate(username=nome_us, password=senha_us)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha Inválidos ou não existem!")
        return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    """ filtrar já com usuário
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    """

    # trazendo todos os registros da tabela
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
