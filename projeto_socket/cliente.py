#!/usr/bin/python3

#Para a o Socket
import socket
import tqdm
import os

def transfer(data):
    #Começo do cliente.py:
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096 # send 4096 bytes each time step
# IP Servidor:
    host = "127.0.0.1"

#Porta:
    port = 5001

#definindo o arquivo que será enviado.
    filename = data

#Tamanho do Arquivo:
    filesize = os.path.getsize(filename)

#Cliente Socket:
    s = socket.socket()

#Conexão:

    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

#Enviar o filername e o filesize:
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

#Começando enviar o arquivo:
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
        
# Lendo os bytes do arquivo:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
            
#Transmissão feita:
                break
        
#Disponibilidade:
            s.sendall(bytes_read)
        
# Progresso:
            progress.update(len(bytes_read))

#Fim:
    s.close()

