from tkinter import *

def verificar(entrada,resultado):
    resultado.config(text='')
    number = entrada.get()
    entrada.delete(0, END)
    try:
        int_number = int(number)
        resultado.config(text='tipo inteiro')
    except:
        try:
            float_number =float(number)
            resultado.config(text='tipo real')
        except:
            try:
                bool_number = bool(number)
                resultado.config(text='tipo booleano')
            except:
                resultado.config(text=f'Não foi possível converter pois o dado é do tipo {type(number)}')
    resultado.pack()