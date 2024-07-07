from tkinter import * 

janela=Tk()
janela.title('Calculadora Simples')


entrada = Entry(janela, width=35, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def click(numero):
    atual = entrada.get()
    entrada.delete(0,END)
    entrada.insert(0, str(atual) + str(numero))
    

def limpar():
    entrada.delete(0, END)


def adiciona():
    primeiro = entrada.get()
    global p_num
    p_num = int(primeiro)
    entrada.delete(0, END)


def igual():
    segundo_numero = entrada.get()
    entrada.delete(0,END)
    entrada.insert(0, p_num + int(segundo_numero))

# definindo botões

bot_1 = Button(janela, text='1', padx=40, pady=20, command=lambda: click(1))
bot_2 = Button(janela, text='2', padx=40, pady=20, command=lambda: click(2))
bot_3 = Button(janela, text='3', padx=40, pady=20, command=lambda: click(3))
bot_4 = Button(janela, text='4', padx=40, pady=20, command=lambda: click(4))
bot_5 = Button(janela, text='5', padx=40, pady=20, command=lambda: click(5))
bot_6 = Button(janela, text='6', padx=40, pady=20, command=lambda: click(6))
bot_7 = Button(janela, text='7', padx=40, pady=20, command=lambda: click(7))
bot_8 = Button(janela, text='8', padx=40, pady=20, command=lambda: click(8))
bot_9 = Button(janela, text='9', padx=40, pady=20, command=lambda: click(9))
bot_0 = Button(janela, text='0', padx=40, pady=20, command=lambda: click(0))
bot_ad = Button(janela, text='+', padx=39, pady=20, command=adiciona)
bot_ig = Button(janela, text='=', padx=91, pady=20, command=igual)
bot_lim = Button(janela, text='Clear', padx=79, pady=20, command=limpar)
# colocar botões no lugar

bot_1.grid(row=3,column=0)
bot_2.grid(row=3,column=1)
bot_3.grid(row=3,column=2)

bot_4.grid(row=2,column=0)
bot_5.grid(row=2,column=1)
bot_6.grid(row=2,column=2)

bot_7.grid(row=1,column=0)
bot_8.grid(row=1,column=1)
bot_9.grid(row=1,column=2)

bot_0.grid(row=4,column=0)
bot_lim.grid(row=4,column=1,columnspan=2)
bot_ad.grid(row=5,column=0)
bot_ig.grid(row=5,column=1,columnspan=2)





janela.mainloop()