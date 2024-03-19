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

        # abrindo arquivo criptografado
        with open(nome_arquivo, 'rb') as arquivo_encrypted:
            encrypted = arquivo_encrypted.read()

        nome_cortado = nome_arquivo.split('__')
        parte1 = nome_cortado[0]
        parte2 = nome_cortado[1].split('.')[-1]
        nome_original = parte1 + '.' + parte2

        # pegando ids para comparação (medida de segurança)
        id_chave = nome_arq_chave.split('_')[-1]
        id_chave = id_chave.split('.')[-2]
        id_arq_criptografado = nome_cortado[1].split('.')[-2]

        if id_chave == id_arq_criptografado:
            # descriptografando arquivo
            decrypted = fernet.decrypt(encrypted)

            # salvando arquivo descriptografado
            with open(nome_original, 'wb') as arquivo_decrypted:
                arquivo_decrypted.write(decrypted)

            # deletando arquivo criptografado
            os.remove(nome_arquivo)
            messagebox.showinfo(title='Sucesso!', message='O arquivo foi descriptografado com sucesso!')

        else:
            messagebox.showwarning(title='Alerta', message='Você está utilizando a chave errada!')

    except Exception as erro:
        messagebox.showerror(title='Erro', message=erro)


if __name__ == '__main__':
    nome_arquivo = input('Insira o nome/caminho do arquivo: ')
    nome_arq_chave = input('Insira o nome do arquivo que contém a chave')
    descriptografar(nome_arquivo, nome_arq_chave)