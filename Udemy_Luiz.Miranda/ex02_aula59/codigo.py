from tkinter import PhotoImage, Label

def horario(entrada, Header,imagens):
    hora = int(entrada.get())
    Header.image=None
    if hora > 0 and hora <= 5:
        Header.config(image=imagens['Tá tarde'])
    elif hora > 5 and hora <= 11:
        Header.config(image=imagens['Bom dia'])
    elif hora > 11 and hora < 13:
        print('Horário de almoço, bora comer')
    elif hora > 13 and hora <= 18:
        Header.config(image=imagens['Café'])
    elif hora > 18 and hora <= 22:
        print('Boa noite, bora jantar ?')
    elif hora > 22 and hora <= 24:
        Header.config(image=imagens['Vai dormir'])
    else:
        Header.config(image=imagens['Banner'])