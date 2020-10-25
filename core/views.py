from django.shortcuts import render, redirect
from .models import Evento


# def index(request):
#     return redirect('/agenda')


def lista_eventos(request):
    eventos = Evento.objects.all()
    response = {'eventos': eventos}
    return render(request, 'agenda.html', response)