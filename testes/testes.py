import socket


HOST = '2a03:2880:f105:283:face:b00c:0:25de'
PORT = 80
time_seconds = 1
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.settimeout(time_seconds)
resultado = sock.connect_ex((HOST, PORT))
print(resultado)



if resultado == 0:
    # O retorno 0 nos diz que a conexão aconteceu, então a porta está aberta.
    print('Aberta')
elif resultado == 10035:
    # O retorno 10035 diz que a conexão não aconteceu.
    print('Fechada')
else:
    # Usei o else aqui para um possível retorno 10060 ou com um
    # outro código de erro que venha surgir na hora da conexão.
    print('Fechada')

