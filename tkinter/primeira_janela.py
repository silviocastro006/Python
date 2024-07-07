from tkinter import *
from time import sleep

# criação da janela principal
janela = Tk()

# determinar o título da janela
janela.title('Minha primeira janela')

# Tamanho da janela + posição na tela do computador
janela.geometry('300x300+10+10')

# redimensionamento da janela (aceita apenas True ou False), só posso aumentar a altura
janela.resizable(False, '400')

# definindo o .ico
janela.iconbitmap(r'tkinter\tech.ico')

# cores da janela
janela.config(background='lightblue')

# função para fechar a janela
def fecha():
    global label1, countdown
    label1 = Label(janela, text='Fechando a janela em 3', foreground='white', background='lightblue')
    label1.pack()
    countdown = 3
    atualizar_contagem()

# função para atualizar a contagem
def atualizar_contagem():
    global countdown
    if countdown > 0:
        label1.config(text=f'Fechando a janela em {countdown}')
        countdown -= 1
        janela.after(1000, atualizar_contagem)
    else:
        janela.destroy()

# definindo o protocolo de fechamento
janela.protocol("WM_DELETE_WINDOW", fecha)


# loop da janela
janela.mainloop()