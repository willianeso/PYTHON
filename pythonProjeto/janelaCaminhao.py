import tkinter as tk
from tkinter import messagebox

# Funções para os botões
def inserir():
    # Validação dos campos
    for campo, entrada in campos.items():
        if not entrada.get().strip():
            messagebox.showwarning("Aviso", f"O campo '{campo}' deve ser preenchido.")
            entrada.focus()
            return
    messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
    limpar_campos()

def pesquisar():
    messagebox.showinfo("Pesquisar", "Botão Pesquisar clicado.")

def alterar():
    messagebox.showinfo("Alterar", "Botão Alterar clicado.")

def excluir():
    messagebox.showinfo("Excluir", "Botão Excluir clicado.")

def limpar_campos():
    for entrada in campos.values():
        entrada.delete(0, tk.END)

# Criar janela principal
janela = tk.Tk()
janela.title("Cadastro de Caminhões")
janela.geometry ("500x500+750+200") #tamanho e posição da janela
janela.minsize(200,200) #tamaho minimo da janela
janela.maxsize(600,600)
janela.resizable(False, False)  # Janela não redimensionável
janela ['bg'] = "OrangeRed"

# Configuração do título
titulo = tk.Label(janela, text="Cadastro de Caminhões", font=("Arial", 16, "bold"), bg = "OrangeRed")
titulo.pack(pady=10)

# Dicionário para armazenar os campos e entradas
campos = {}

# Lista de campos
nomes_campos = [
    "Modelo",
    "Marca",
    "Cor",
    "Placa",
    "Renavam",
    "Chassi",
    "Capacidade (kg)",
    "Quantidade"
]

# Criar os campos de entrada
frame_campos = tk.Frame(janela,bg = "OrangeRed")
frame_campos.pack(pady=10)

for nome in nomes_campos:
    label = tk.Label(frame_campos, text=f"{nome}:", font=("Arial", 12), bg = "OrangeRed")
    label.grid(row=nomes_campos.index(nome), column=0, sticky="e", padx=5, pady=2)
    
    entrada = tk.Entry(frame_campos, width=30, font=("Arial", 12))
    entrada.grid(row=nomes_campos.index(nome), column=1, pady=2)
    campos[nome] = entrada

# Criar botões
frame_botoes = tk.Frame(janela,bg = "OrangeRed")
frame_botoes.pack(pady=20)

botao_inserir = tk.Button(frame_botoes, text="Inserir", font=("Arial", 12), width=10, command=inserir, bg = "#FF8C00")
botao_inserir.grid(row=0, column=0, padx=5)

botao_pesquisar = tk.Button(frame_botoes, text="Pesquisar", font=("Arial", 12), width=10, command=pesquisar)
botao_pesquisar.grid(row=1, column=0, padx=5)

botao_alterar = tk.Button(frame_botoes, text="Alterar", font=("Arial", 12), width=10, command=alterar)
botao_alterar.grid(row=0, column=1, padx=5)

botao_excluir = tk.Button(frame_botoes, text="Excluir", font=("Arial", 12), width=10, command=excluir)
botao_excluir.grid(row=1, column=1, padx=9)

# Rodar a aplicação
janela.mainloop()
