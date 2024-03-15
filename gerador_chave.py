from cryptography.fernet import Fernet


def gerar_chave():
    # gera a chave
    chave = Fernet.generate_key()

    # salva a chave em arquivo externo
    with open('arquivo_chave.key', 'wb') as arquivo_chave:
        arquivo_chave.write(chave)


if __name__ == '__main__':
    gerar_chave()