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


@login_required(login_url='/login/')
def cadevento(request):
    id_evento = request.GET.get('id')
    dados_recebidos = {}
    if id_evento:
        dados_recebidos['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'cevento.html', dados_recebidos)


@login_required(login_url='/login/')
def salvar_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        local_evento = request.POST.get('local_evento')
        usuario = request.user
        alterando = request.POST.get('id_alterando')

        if alterando:
            eventoalteracao = Evento.objects.get(id=alterando)
            if eventoalteracao.usuario == usuario:
                eventoalteracao.titulo = titulo
                eventoalteracao.data_evento = data_evento
                eventoalteracao.descricao = descricao
                eventoalteracao.local_evento = local_evento
                eventoalteracao.save()

            # ---------------------------------------
            """SEGUNDA FORMA DE GRAVAR AS ALTERAÇÕES"""
            # Evento.objects.filter(id=alterando).update(titulo=titulo,
            #                                           data_evento=data_evento,
            #                                           descricao=descricao,
            #                                           local_evento=local_evento)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  local_evento=local_evento,
                                  usuario=usuario)
    return redirect('/')


@login_required(login_url='/login/')
def deletar_evento(request, id_evento):
    usuario = request.user
    evento_atual = Evento.objects.get(id=id_evento)
    if usuario == evento_atual.usuario:
        evento_atual.delete()
    return redirect('/')
