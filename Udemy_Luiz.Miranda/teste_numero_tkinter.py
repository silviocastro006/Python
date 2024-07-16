# 1 - Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

from tkinter import * 

def par_impar(num):
    global resposta
    global resp
    if num % 2 == 0:
        resposta = 'Par'
    else:
        resposta = 'Impar'
    resp.config(text=f'O número inserido é {resposta}')
    resp.pack()



def submit():
    global numero
    numero = entrada.get()
    verificar()

def verificar():
    global numero
    if numero.isdigit():
        numero = int(numero)
        validar = par_impar(numero)
    else:
        resposta = Label(master=janela, text=f'O valor digitado não é inteiro, ele é {type(numero)}')
        resposta.pack()

janela = Tk()
janela.geometry("350x350")
janela.resizable(False,False)
janela.title('Verificador de número')

enunciado = Label(
    master=janela,
    text='Este mini programa verifica se o número é inteiro, par ou ímpar. Se não for ele informa o motivo',
    wraplength=330,
    justify='left',
    pady=20
)


entrada = Entry(
    master=janela,
    width=20,

)


bot = Button(
    master=janela,
    width=10,
    height=5,
    command=submit,
    text='Verificar',
    justify='right'
)


resposta = None
numero = entrada.get()
entrada.config()
enunciado.pack()
entrada.pack()
bot.pack()

resp = Label(
    master=janela,
    text=f'O número digitado é {resposta}'
)


janela.mainloop()
