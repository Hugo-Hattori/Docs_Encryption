from cryptography.fernet import Fernet

# gera a chave
chave = Fernet.generate_key()

# salva a chave em arquivo externo
with open('arquivo_chave.key', 'wb') as arquivo_chave:
    arquivo_chave.write(chave)