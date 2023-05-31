import tkinter as tk
from tkinter import filedialog
from antlr4 import *
from gen.tweets_grammarLexer import tweets_grammarLexer
from gen.tweets_grammarParser import tweets_grammarParser

def processar_entrada():
    entrada = entrada_texto.get("1.0", "end-1c")  # Obtém o texto da caixa de texto

    # Cria um objeto de entrada para o analisador léxico do ANTLR
    input_stream = InputStream(entrada)
    lexer = tweets_grammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Cria um objeto de parser para o analisador sintático do ANTLR
    parser = tweets_grammarParser(token_stream)
    tree = parser.tweet()

    # Obtenha o resultado do processamento
    resultado = tree.toStringTree(recog=parser)

    # Exiba o resultado na janela
    resultado_texto.delete("1.0", "end")  # Limpa o widget de texto
    resultado_texto.insert("1.0", resultado)

def carregar_arquivo():
    arquivo = tk.filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if arquivo:
        with open(arquivo, "r") as file:
            texto = file.read()
        entrada_texto.delete("1.0", "end")  # Limpa o widget de texto
        entrada_texto.insert("1.0", texto)

janela = tk.Tk()
janela.title("ANTLR4 TWEETS")

# Cria a caixa de texto de entrada
entrada_texto = tk.Text(janela, height=10, width=50)
entrada_texto.pack()

# Cria o botão de carregar arquivo
botao_carregar = tk.Button(janela, text="Carregar Arquivo", command=carregar_arquivo)
botao_carregar.pack()

# Cria o botão de processar
botao_processar = tk.Button(janela, text="Processar", command=processar_entrada)
botao_processar.pack()

# Cria o widget de texto para exibir o resultado
resultado_texto = tk.Text(janela, height=10, width=50)
resultado_texto.pack()

# Inicia o loop principal da janela
janela.mainloop()