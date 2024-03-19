from cryptography.fernet import Fernet
from datetime import datetime
from tkinter import messagebox


def gerar_chave():
    # gera a chave
    chave = Fernet.generate_key()

    # usar datetime para criar uma chave única
    agora = datetime.now().timestamp()
    agora = str(int(round(agora)))
    nome_chave_arquivo = 'arquivo_chave_' + agora + '.key'

    # salva a chave em arquivo externo
    with open(nome_chave_arquivo, 'wb') as arquivo_chave:
        arquivo_chave.write(chave)
    messagebox.showinfo(title='Sucesso!', message='Uma nova chave foi gerada com sucesso!')


if __name__ == '__main__':
    gerar_chave()