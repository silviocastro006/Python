from tkinter import *
import os

cont = 1
def cadastro():
    jan_cadas = Tk()
    jan_cadas.geometry('330x230')
    jan_cadas.config(background='#00BFFF', padx=10, pady=10)
    jan_cadas.title('Cadastro de alunos')
    jan_cadas.iconbitmap(bitmap=r'tkinter\primeiro_app.py\tech.ico')

    info = Label(master=jan_cadas, text='Favor cadastrar nomes abaixo',background='#00BFFF', foreground='black', pady=10).grid(row=0, column=0)

    espac1 = Label(master=jan_cadas, background='#00BFFF').grid(row=1, column=0)

    def obter_caminho(): #obtenho o caminho genérico
        diretorio = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(diretorio,'cadastro.txt')
    
    caminho = obter_caminho()

    def criar_arquivo(caminho): # crio o arquivo caso não exista
        with open(caminho,'a'):
            pass

    criar_arquivo(caminho)

    def cadastrar():
        global cont
        nome = dados.get()
        arquivo = open(caminho, 'a')
        arquivo.write(f'{cont} ) {nome}\n')
        dados.delete(0,END)
        cont += 1
        arquivo.close()


    def fechar():
        jan_cadas.destroy()


    dados = Entry(master=jan_cadas, background='white', justify='left', width=50)
    dados.grid(row=1, column=0)



    espac2 = Label(master=jan_cadas, background='#00BFFF').grid(row=3, column=0)

    cadastro = Button(master=jan_cadas, text='Cadastrar', padx=20, pady=20, command=cadastrar).grid(row=4, column=0)

    sair = Button(master=jan_cadas, text='Sair', padx=35, pady=20, command=fechar).grid(row=5, column=0)

    jan_cadas.mainloop()