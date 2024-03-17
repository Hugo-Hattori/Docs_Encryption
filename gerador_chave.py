from cryptography.fernet import Fernet
from datetime import datetime


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


if __name__ == '__main__':
    gerar_chave()