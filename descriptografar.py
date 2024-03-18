from cryptography.fernet import Fernet
import os
from tkinter import messagebox


def descriptografar(nome_arquivo, nome_arq_chave):
    try:
        # abrindo a chave
        with open(nome_arq_chave, 'rb') as arquivo_chave:
            chave = arquivo_chave.read()

        # utilizando a chave gerada
        fernet = Fernet(chave)

        # abrir arquivo criptografado
        with open(nome_arquivo, 'rb') as arquivo_encrypted:
            encrypted = arquivo_encrypted.read()

        # descriptografar
        decrypted = fernet.decrypt(encrypted)

        # salva arquivo descriptografado
        nome_cortado = nome_arquivo.split('__')
        parte1 = nome_cortado[0]
        parte2 = nome_cortado[1].split('.')[-1]
        nome_original = parte1 + '.' + parte2
        with open(nome_original, 'wb') as arquivo_decrypted:
            arquivo_decrypted.write(decrypted)

        # deletado arquivo criptografado
        os.remove(nome_arquivo)

    except Exception as erro:
        print(erro)
        messagebox.showerror(title='Erro', message=erro)


if __name__ == '__main__':
    nome_arquivo = input('Insira o nome/caminho do arquivo: ')
    nome_arq_chave = input('Insira o nome do arquivo que contém a chave')
    descriptografar(nome_arquivo, nome_arq_chave)