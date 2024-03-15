from cryptography.fernet import Fernet


def descriptografar(nome_arquivo):
    # abrindo a chave
    with open('arquivo_chave.key', 'rb') as arquivo_chave:
        chave = arquivo_chave.read()

    # utilizando a chave gerada
    fernet = Fernet(chave)

    # abrir arquivo criptografado
    with open(nome_arquivo, 'rb') as arquivo_encrypted:
        encrypted = arquivo_encrypted.read()

    # descriptografar
    decrypted = fernet.decrypt(encrypted)

    # sobreescrevendo arquivo descriptografado
    with open(nome_arquivo, 'wb') as arquivo_decrypted:
        arquivo_decrypted.write(decrypted)


if __name__ == '__main__':
    nome_arquivo = input('Escreva o nome/caminho do arquivo: ')
    descriptografar(nome_arquivo)