# Importação do tkinter
from tkinter import *

# Configuração da janela inicial
root = Tk()
root.title('Calculadora Simples')
entrada = Entry(root, width=35, borderwidth=3)
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Criação de função para o botão


# Criação dos botões
bot1 = Button(root, text='1', padx=40, pady=20,command=clique)
bot2 = Button(root, text='2', padx=40, pady=20,command=clique)
bot3 = Button(root, text='3', padx=40, pady=20,command=clique)
bot4 = Button(root, text='4', padx=40, pady=20,command=clique)
bot5 = Button(root, text='5', padx=40, pady=20,command=clique)
bot6 = Button(root, text='6', padx=40, pady=20,command=clique)
bot7 = Button(root, text='7', padx=40, pady=20,command=clique)
bot8 = Button(root, text='8', padx=40, pady=20,command=clique)
bot9 = Button(root, text='9', padx=40, pady=20,command=clique)
bot0 = Button(root, text='0', padx=40, pady=20,command=clique)
bot_ad = Button(root, text='+', padx=39, pady=20,command=clique)
bot_ig = Button(root, text="=", padx=91, pady=20,command=clique)
bot_cl = Button(root, text='Clear', padx=79, pady=20,command=clique)

# Organizando os botões na tela

bot7.grid(row=1, column=0)
bot8.grid(row=1, column=1)
bot9.grid(row=1, column=2)

bot4.grid(row=2, column=0)
bot5.grid(row=2, column=1)
bot6.grid(row=2, column=2)

bot1.grid(row=3, column=0)
bot2.grid(row=3, column=1)
bot3.grid(row=3, column=2)

bot0.grid(row=4, column=0)
bot_cl.grid(row=4, column=1, columnspan=2)
bot_ad.grid(row=5, column=0)
bot_ig.grid(row=5, column=1, columnspan=2)

root.mainloop()