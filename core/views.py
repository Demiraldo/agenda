# primeira forma de redirecionar o index para uma outra view
# from django.shortcuts import render, redirect

from django.shortcuts import render
from core.models import Evento


# primeira forma para redirecionar o index para outra view
# def index(request):
#    return redirect('/agenda/')


def lista_eventos(request):
    """ filtrar já com usuário
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    """

    # trazendo todos os registros da tabela
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
