import tkinter as tk

janela = tk.Tk()
janela.title("Objetos posicionados")
janela.geometry("300x200")

# Colocando widgets um embaixo do outro
tk.Label(janela, text="Nome:").place(x=20, y=20)
tk.Entry(janela).place(x=10, y=50)
tk.Button(janela, text="Enviar").place(x=20, y=80)

janela.mainloop()