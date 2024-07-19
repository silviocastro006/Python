from tkinter import *

def verificar(janela,entrada,resultado):
    if resultado== '':
        pass
    else:
        resultado.config(text='')
        number = entrada.get()
        entrada.delete(0, END)
        if isinstance(number,str):
            number = number.upper()
        try:
            int_number = int(number)
            resultado.config(text=f'{int_number} é do tipo inteiro')
        except:
            try:
                float_number =float(number)
                resultado.config(text=f'{float_number} é do tipo real')
            except:
                try:
                    if number == 'FALSE':
                        bool_number = False
                    elif number == 'TRUE':
                        bool_number = True
                    resultado.config(text=f'{bool_number} é do tipo booleano')
                except:
                    resultado.config(text=f'Não foi possível converter pois {number} é do tipo {type(number)}')
        janela.geometry('400x250')
        resultado.pack(side='bottom')