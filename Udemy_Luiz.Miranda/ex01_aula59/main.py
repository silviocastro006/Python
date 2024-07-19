# 1 - Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro

#importação do módulo
from tkinter import * 
from tkinter import ttk as ttk
from funcoes import verificar

# configuração da janela principal
janela =  Tk()
janela.title('Verificador de números')
janela.iconbitmap(bitmap=r'Udemy_Luiz.Miranda\ex01_aula59\artificial-intelligence.ico')
janela.geometry('400x180')
janela.config(
    pady=10,
    padx=10
)

# criação dos widgets

titulo = Label(
    master=janela,
    text='Verificador de números',
    anchor='center',
    height=1,
    width=42,
    background='white',
    padx=10,
    pady=10,
    font=('system',4)
)

entrada = Entry(
    master=janela,
    relief='solid',
    width=30,
    justify='center',
)

resultado = Label(
    master=janela,
    height=4,
    width=100,
    background='white'
)


botao =  Button(
    master=janela,
    text='Analisar',
    height=3,
    width=10,
    relief='groove',
    background='#DDA0DD',
    borderwidth=3,
    activebackground='#C71585',
    command=verificar()
)

separador = Frame(
    master=janela,
    width=360,
    height=3,
    background='lightgrey'
)


# organização dos widgets na tela
titulo.place(x=10, y=5 )
entrada.place(x=10, y=92)
botao.place(x=250,y=72)


janela.mainloop()