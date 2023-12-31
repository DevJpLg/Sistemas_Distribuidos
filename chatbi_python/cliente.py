import socket
import threading

# Utilização do host com endereço local e uma porta aleatória
HOST = '127.0.0.1'
PORTA = 7777

apelido = input("Digite o seu nome: ")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #define o socket do cliente nos protocolos (TCP/IP) e se conecta ao servidor
cliente.connect((HOST, PORTA))

def receber(): #Recebe e imprime mensagens de um servidor de chat
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            if mensagem == 'apelido':
                cliente.send(apelido.encode('utf-8'))
            else:
                print(mensagem)
        except:
            cliente.close()
            break

def escrever(): #Envia mensagens digitadas pelo usuário para um servidor de chat
    while True:
        try:
            mensagem = input('')
            cliente.send(mensagem.encode('utf-8'))
        except KeyboardInterrupt:
            break

receber_thread = threading.Thread(target=receber) #Uma thread é criada para a função receber
receber_thread.start()

escrever() #Por último, a função escrever é chamada para permitir que o usuário envie mensagens
