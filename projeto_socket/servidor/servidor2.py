#!/usr/bin/python3

import socket
import tqdm
import os

#IP dos dispositivo:
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001

#Definindo que o servidor receba 4096 por vez:
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

#Criando o Socket:
s = socket.socket()

#Vinculando o endereço e a porta:
s.bind((SERVER_HOST, SERVER_PORT))

#Número de conexeões e escuta:
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

#Aceitar conexões no servidor:
client_socket, address = s.accept()

#Conexão feita:
print(f"[+] {address} is connected.")

#Recebendo o arquivo do cliente:
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

#Remover possível caminho absoluto
filename = os.path.basename(filename)

#conversão para inteiro.
filesize = int(filesize)

#começando a receber

progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))
client_socket.close()
s.close()
            
