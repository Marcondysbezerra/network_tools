from .forms import TestePortaForm
from django.shortcuts import render
import socket
import requests


def teste_de_portas(request):
    # Tempo de resposta para a conexão.
    time_seconds = 1
    # Validação dos campos do formulário.
    if request.method == 'POST':
        form = TestePortaForm(request.POST)
        if form.is_valid():
            ip = form.cleaned_data.get('ip')
            porta = form.cleaned_data.get('porta')
            # Conexão com o servidor TCP.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(time_seconds)
            result = sock.connect_ex((ip, porta))

            context = {
                'result': result, 'form': form, 'ip': ip, 'porta': porta
            }
            return render(request, 'myapp/teste_de_portas.html', context)
    form = TestePortaForm()

    return render(request, 'myapp/teste_de_portas.html', {'form': form})


def ip_externo(request):
    # Api para consulta de IPv4 externo.
    ip_externo = requests.get('https://api.ipify.org/').text
    return render(request, 'myapp/teste_de_portas.html', {'ip_externo': ip_externo})


def ip_externo_six(request):
    # Api para consulta de IPv6 externo.
    ip_externo_six = requests.get('https://api6.ipify.org/').text
    return render(request, 'myapp/teste_de_portas.html', {'ip_externo_six': ip_externo_six})



