#!/usr/bin/python3


#Importando funções dos arquivos dos projetos.
from time import sleep
from cliente import transfer
from comprimir import ziper
from ler import ls_l 
from criptografia import load_key 
from criptografia import encrypt 

#Menu:

opc = 0
while opc != 4:
    print('''[ 1 ] Enviar arquivo.
[ 2 ] Compactar arquivo.
[ 3 ] Criptografar arquivo.
[ 4 ] Sair.''')
    opc = int(input('Digite uma das opções acima: '))

#Chamando a função transfer de cliente.py
    if opc == 1:
        ls_l()
        file = input("Digite o nome do arquivo: ")
        transfer(file)
    elif opc == 2:
        ls_l()
        dir = input("Caminho do diretório a ser zipado: ")
        zipname = input("Nome do arquivo .zip (sem .zip): ")
        savepath = input(f"Caminho para salvar o arquivo {zipname}.zip localmente antes de enviar: ")
        ziper(zipname, savepath, dir)
    elif opc == 3: 
        ls_l()
        filename = input("Digite o nome do arquivo: ")
        key = load_key()
        encrypt(filename, key)
    else:
        print('Opção não reconhecida')
    sleep(3)
print('Programa encerrado.')
