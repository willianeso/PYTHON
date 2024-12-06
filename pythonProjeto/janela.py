#interface grafica com TKinter


from tkinter import * 
from tkinter import messagebox

janela =  Tk()
janela.title ("Primeira janela")
janela.geometry ("500x500+750+200") #tamanho e posição da janela
janela.minsize(200,200) #tamaho minimo da janela
janela.maxsize(600,600) #tamanho maximo da tela
janela.resizable(False, False) # para desabilitar o botão de maximizar ou minimizar
#janela.state("zoomed") # para iniciar em tela em tela cheia
#janela.state("iconic") # para iniciar em tela minimizada, o usuário não verá a janela
janela ['bg'] = "OrangeRed" #cor de fundo da janela

def mensagem1():
    texto = txtnome.get()
    print(texto)
    
def mensagem2():
    messagebox.showinfo("Informação", "Avisei para não clicar") #menssagem de informação
    
def mensagem3():
    messagebox.showwarning("Antenção", "Cuidado com o vírus") #menssagem de atenção

def mensagem4():
    messagebox.showerror("Erro", "Deu tudo errado") #menssagem de erro

#adiciona um label (tótulo)
nome = Label (janela,text = "Nome", font = "Arial 20 bold", bg = "#8FBC8F", fg = "#556B2F") # fonte e tamanho de fonte, o bg muda cor
nome.pack()  # cria a label

#adiciona caixa de texto
txtnome = Entry (janela, font = "Arial 15")
txtnome.pack()

#adicionar botão
btn1 = Button (janela, text = "Enviar", font = "Arial 15", command = mensagem1)
btn1.pack()

btn2 = Button (janela, text = "Menssagem de informação", font = "Arial 15", command = mensagem2)
btn2.pack()

btn3 = Button (janela, text = "Menssagem de atenção", font = "Arial 15", command = mensagem3)
btn3.pack()

btn4 = Button (janela, text = "Menssagem de erro", font = "Arial 15", command = mensagem4)
btn4.pack()


janela.mainloop()