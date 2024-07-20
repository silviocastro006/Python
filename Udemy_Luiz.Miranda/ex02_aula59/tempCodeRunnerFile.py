from tkinter import * 
from time import *
from tkinter.font import Font
from codigo import horario

root = Tk()
root.geometry('600x400')
root.title('Verificador de horário')
root.iconbitmap(bitmap=r'Udemy_Luiz.Miranda\ex02_aula59\imagens\clock.ico')


fundo_painel = LabelFrame(
    master=root,
    text='Painel de Controle',
    bg='#87b5b8',
    width=500,
    height=150
)

imagem = Frame(
    master=root,
    height=210,
    width=500,
    background=PhotoImage(file=r'Udemy_Luiz.Miranda\ex02_aula59\imagens\bom_dia.png')
)

entrada = Entry(
    master=fundo_painel,
    width=20
)

informativo = Label(
    master=fundo_painel,
    text='Insira um horário',
    borderwidth=1,
    background='#205c5f',
    width=15,
    height=2,
    relief='solid',
    fg='white',
    font=Font(family='Helvetiva', size=10, weight='bold')
)

botao_env = Button(
    master=fundo_painel,
    width=12,
    heigh=2,
    text='Verificar',
    relief='groove',
    background='#5fbf1e',
    fg='white',
    font=Font(family='Helvetiva', size=10, weight='bold'),
    activebackground='#447b1d',
    command=lambda: horario(entrada)
)

botao_sair = Button(
    master=fundo_painel,
    width=12,
    heigh=2,
    text='Sair',
    relief='groove',
    background='#b93c3c',
    fg='white',
    font=Font(family='Helvetiva', size=10, weight='bold'),
    activebackground='#762626'
)

fundo_painel.place(x=50,y=240)
imagem.place(x=50,y=20)
entrada.place(x=250, y=30)
informativo.place(x=120,y=22)
botao_env.place(x=255,y=80)
botao_sair.place(x=140, y=80)
root.mainloop()