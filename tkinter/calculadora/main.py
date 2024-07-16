# Importação do tkinter
from tkinter import *

# Configuração da janela inicial
root = Tk()
root.title('Calculadora +')
entrada = Entry(root, width=35, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=3, padx=9, pady=9)
root.resizable(False,False)

# variáveis
p_num = None

# Criação de função para o botão
def clique(num):
    atual = entrada.get()
    entrada.delete(0,END)
    entrada.insert(0,str(atual)+str(num))

def limp():
    entrada.delete(0,END)

def adiciona():
    primeiro = entrada.get()
    global p_num
    p_num = int(primeiro)
    entrada.delete(0,END)

def igual():
    registro = entrada.get()
    segundo = int(registro)
    entrada.delete(0,END)
    entrada.insert(0, p_num+segundo)




# Criação dos botões
bot1 = Button(root, text='1', width=10, height=3,padx=2,command=lambda: clique(1))
bot2 = Button(root, text='2', width=10, height=3,padx=2,command=lambda: clique(2))
bot3 = Button(root, text='3', width=10, height=3,padx=2,command=lambda: clique(3))
bot4 = Button(root, text='4', width=10, height=3,padx=2,command=lambda: clique(4))
bot5 = Button(root, text='5', width=10, height=3,padx=2,command=lambda: clique(5))
bot6 = Button(root, text='6', width=10, height=3,padx=2,command=lambda: clique(6))
bot7 = Button(root, text='7', width=10, height=3,padx=2,command=lambda: clique(7))
bot8 = Button(root, text='8', width=10, height=3,padx=2,command=lambda: clique(8))
bot9 = Button(root, text='9', width=10, height=3,padx=2,command=lambda: clique(9))
bot0 = Button(root, text='0', width=10, height=3,padx=2,command=lambda: clique(0))
bot_ad = Button(root, text='+',padx=2, width=10, height=3,command=adiciona)
bot_ig = Button(root, text='=',width=22, height=3,command=igual())
bot_cl = Button(root, text='Clear', width=22, height=3,command=limp)

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