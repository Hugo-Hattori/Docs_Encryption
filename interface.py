import tkinter as tk
from tkinter.filedialog import askopenfilename
from gerador_chave import gerar_chave
from criptografar import criptografar
from descriptografar import descriptografar


def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title="Selecione o arquivo que deseja criptografar")
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivoselecionado['text'] = f"Arquivo Selecionado: {caminho_arquivo}"
        global arquivo_selecionado
        arquivo_selecionado = var_caminhoarquivo.get()


janela = tk.Tk()

janela.title('Criptografia de Arquivos')

var_caminhoarquivo = tk.StringVar()

botao_selecionararquivo = tk.Button(text="Clique para Selecionar", command=selecionar_arquivo)
botao_selecionararquivo.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

label_arquivoselecionado = tk.Label(text='Nenhum Arquivo Selecionado', anchor='e')
label_arquivoselecionado.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

botao_gerar_chave = tk.Button(text="Criptografar", command=lambda: criptografar(nome_arquivo=arquivo_selecionado))
botao_gerar_chave.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

botao_gerar_chave = tk.Button(text="Descriptografar", command=lambda: descriptografar(nome_arquivo=arquivo_selecionado))
botao_gerar_chave.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

botao_gerar_chave = tk.Button(text="Clique para gerar uma nova chave", command=gerar_chave)
botao_gerar_chave.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')


janela.mainloop()