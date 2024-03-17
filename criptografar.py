from cryptography.fernet import Fernet


def criptografar(nome_arquivo, nome_arq_chave):
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

    # sobrescrevendo dados criptografados
    with open(nome_arquivo, 'wb') as arquivo_encrypted:
        arquivo_encrypted.write(encrypted)


if __name__ == '__main__':
    nome_arquivo = input('Insira o nome/caminho do arquivo: ')
    nome_arq_chave = input('Insira o nome do arquivo que contém a chave')
    criptografar(nome_arquivo, nome_arq_chave)