import tkinter as tk
from tkinter.filedialog import askopenfilename
from gerador_chave import gerar_chave
from criptografar import criptografar
from descriptografar import descriptografar


def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title="Selecione o arquivo que deseja criptografar")
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        caminho_arquivo = caminho_arquivo.split('/')[-1]
        label_arquivo_selecionado['text'] = f"Arquivo Selecionado: \n {caminho_arquivo}"
        global arquivo_selecionado
        arquivo_selecionado = var_caminhoarquivo.get()


def selecionar_chave():
    caminho_arquivo = askopenfilename(title="Selecione a chave que ira criptografar/descriptografar")
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        caminho_arquivo = caminho_arquivo.split('/')[-1]
        label_chave_selecionada['text'] = f"Arquivo Selecionado: \n {caminho_arquivo}"
        global chave_selecionado
        chave_selecionado = var_caminhoarquivo.get()


janela = tk.Tk()

janela.title('Criptografia de Arquivos')

var_caminhoarquivo = tk.StringVar()

botao_selecionar_arquivo = tk.Button(text="Selecionar Arquivo", command=selecionar_arquivo)
botao_selecionar_arquivo.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

label_arquivo_selecionado = tk.Label(text='Nenhum Arquivo Selecionado', anchor='e')
label_arquivo_selecionado.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

botao_selecionar_chave = tk.Button(text="Selecionar Chave", command=selecionar_chave)
botao_selecionar_chave.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

label_chave_selecionada = tk.Label(text='Nenhum Arquivo Selecionado', anchor='e')
label_chave_selecionada.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

botao_gerar_chave = tk.Button(text="Criptografar", command=lambda: criptografar(nome_arquivo=arquivo_selecionado, nome_arq_chave=chave_selecionado))
botao_gerar_chave.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

botao_cryp = tk.Button(text="Descriptografar", command=lambda: descriptografar(nome_arquivo=arquivo_selecionado, nome_arq_chave=chave_selecionado))
botao_cryp.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')

botao_decryp = tk.Button(text="Clique para gerar uma nova chave", command=gerar_chave)
botao_decryp.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

janela.mainloop()