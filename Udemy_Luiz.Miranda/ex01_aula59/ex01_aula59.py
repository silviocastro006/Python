# 1 - Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

from customtkinter import *


# configuração de janela principal
janela = CTk()
janela.iconbitmap(bitmap=r'Udemy_Luiz.Miranda\ex01_aula59\artificial-intelligence.ico')
janela.title('Verificador de número')
janela.geometry('410x230')
janela.resizable(False,False)
janela.configure(fg_color='#C1A7EA', pady=10, padx=10)
janela._set_appearance_mode('light')

def verificar():
    global entrada
    num = entrada.get().upper()

    try:
        num_int= int(num)
        print(f'O dado inserido é do tipo: {type(num_int)}')
        print(num_int)
    except:
        try:
            num_float = float(num)
            print(f'O dado inserido é do tipo: {type(num_float)}')
            print(num_float)
        except:
            try:
                if num == 'TRUE':
                    num_bool = True
                elif num == 'FALSE':
                    num_bool = False
                print(f'O dado inserido é do tipo {type(num_bool)}')
                print(num_bool)
            except:
                print(f'Não foi possível converter pois o dado inserido é do tipo: {type(num)}')
                print(num)

# criar widgets

titulo = CTkLabel(
    master=janela,
    text='Insira um valor no campo abaixo e clique no botão verificar.',
    height=50,
    width=350,
    font=('Arial',13),
    fg_color='white',
    text_color='black',
    padx=15,
    corner_radius=10
)

entrada = CTkEntry(
    master=janela,
    width=300,
    fg_color='white',
    text_color='black',
    placeholder_text='Digite aqui:  '
)

botao = CTkButton(
    master=janela,
    text='Verificar',
    height=50,
    width=10,
    command=lambda: verificar()
)

result = CTkLabel(
    master=janela,
    text=...,
    height=50,
    width=390,
    fg_color='white',
    corner_radius=10
)

# organizar os widgets
titulo.grid(row=0,column=0, columnspan=2, pady=10)
entrada.grid(row=1, column=0, pady=20)
botao.grid(row=1, column=1)
result.grid(row=3, column=0, columnspan=2, pady=20)

# função








# loop principal
janela.mainloop()