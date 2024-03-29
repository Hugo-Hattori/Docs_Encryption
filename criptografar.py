from cryptography.fernet import Fernet
import os
from tkinter import messagebox


def criptografar(nome_arquivo, nome_arq_chave):
    try:
        # confirmar se o usuário deseja criptografar
        mensagem_confirmacao = 'O arquivo selecionado será substituído pela versão criptografada, deseja continuar?'
        confirmacao = messagebox.askokcancel(title='Confirmar criptografia?', message=mensagem_confirmacao)
        if confirmacao:
            # verificar se o arquivo já foi criptografado antes
            try:
                id_chave_ja_usada = nome_arquivo.split('__')[-1]
                id_chave_ja_usada = int(id_chave_ja_usada.split('.')[-2])
                if type(id_chave_ja_usada) == int:
                    messagebox.showwarning(title='Alerta!', message='Este arquivo já está criptografado!')
            # se não estiver criptografado, então criptografa
            except:
                # abrindo a chave
                with open(nome_arq_chave, 'rb') as arquivo_chave:
                    chave = arquivo_chave.read()

                # utilizando a chave gerada
                fernet = Fernet(chave)

                # abrindo arquivo a ser criptografado
                with open(nome_arquivo, 'rb') as arquivo:
                    original = arquivo.read()

                # criptografando arquivo
                encrypted = fernet.encrypt(original)

                # salvando arquivo criptografado
                id_unico = nome_arq_chave.split('_')[-1]
                id_unico = id_unico.split('.')[-2]
                nome_cortado = nome_arquivo.split('.')
                parte1 = nome_cortado[-2]
                parte2 = nome_cortado[-1]
                with open(parte1 + '__' + id_unico + '.' + parte2, 'wb') as arquivo_encrypted:
                    arquivo_encrypted.write(encrypted)

                # deletando arquivo não criptografado
                os.remove(nome_arquivo)
                messagebox.showinfo(title='Sucesso!', message='O arquivo foi criptografado com sucesso!')

    except Exception as erro:
        messagebox.showerror(title='Erro', message=erro)


if __name__ == '__main__':
    nome_arquivo = input('Insira o nome/caminho do arquivo: ')
    nome_arq_chave = input('Insira o nome do arquivo que contém a chave')
    criptografar(nome_arquivo, nome_arq_chave)