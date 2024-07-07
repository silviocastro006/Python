from tkinter import *
from cadastro import *
from ver import *

def fecha():
    janela.destroy()

janela = Tk()
janela.geometry('470x200')
janela.config(bg='#00BFFF', padx=10, pady=10)
janela.iconbitmap(bitmap=r'tkinter\primeiro_app.py\tech.ico')
janela.title('Exemplo de tela de cadastro')


apresent = Label(master=janela, text='Este pequeno app é um teste para gravar certas informações num text e poder visualizar o que está cadastrado.', bg='white', fg='black', justify='left', padx=100, pady=20, wraplength=250).grid(row=0, columnspan=3)
espac = Label(master=janela, background='#00BFFF').grid(row=1,columnspan=3)



bot_1 = Button(master=janela, text='Cadastrar', padx=50, pady=20, command=cadastro).grid(row=2, column=0)
bot_2 = Button(master=janela, text='Visualizar', padx=51, pady=20, command=ver).grid(row=2, column=1)
bot_3 = Button(master=janela, text='Sair', padx=51, pady=20, command=fecha).grid(row=2, column=2)



janela.mainloop()