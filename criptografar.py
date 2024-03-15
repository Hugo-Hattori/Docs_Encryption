from cryptography.fernet import Fernet

nome_arquivo = 'arquivo.txt'

# abrindo a chave
with open('arquivo_chave.key', 'rb') as arquivo_chave:
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