"""
1. Crie um script e nele adicione um dicionário que deverá receber nome e o
telefone de 10 pessoas. Após receber todos os dados, liste os dados
recebidos. Crie uma opção de busca pelo nome, se o nome for encontrado o
telefone será exibido.

"""

"""
Sei que minha solução não é a melhor do mundo, pois o ideal seria em orientação a objeto,
mas estou testando com a biblioteca e já já faço em LPOO

"""

# Importação do tkinter
import tkinter as tk
from PIL import Image, ImageTk

# ========================== Navegação inicial ==============================

def abrir_tela_cadastro(tela):
    tela.destroy()
    cadastro()


def voltar_tela_principal(tela):
    tela.destroy()
    criar_tela_principal()

# ========================== Tela Cadastro ==============================

def cadastro():
    tela_cadastro = tk.Tk()

    tela_cadastro.title('Cadastro de Contatos')

    tela_cadastro.config(
    width=400,
    height=400,
    background='#efd147'
    )

    tela_cadastro.resizable(height=False, width=False)

    label_nome = tk.Label(
        master=tela_cadastro,
        text="Nome",
        bg="#efd147",
        fg="black",
        font=("Arial",30, "bold")
    )

    label_nome.place(x=20, y=50)
    entrada_nome = tk.Entry(tela_cadastro, width=40)
    entrada_nome.place(x=150, y=70)

    label_telefone = tk.Label(
    master=tela_cadastro,
    text="Telefone",
    bg="#efd147",
    fg="black",
    font=("Arial",30, "bold")
    )

    label_telefone.place(x=20, y=120)
    entrada_telefone = tk.Entry(tela_cadastro, width=33)
    entrada_telefone.place(x=190, y=140)



    imsal = Image.open(r"...\Imagens\Salvar.png")
    imsal_tk = ImageTk.PhotoImage(imsal)



    botao2_salvar = tk.Button(
        text="Ver lista telefonica",
        master=tela_cadastro,
        background="#efd147",
        activebackground="#efd147",
        image=imsal_tk,
        borderwidth=0,
    )

    botao2_salvar.place(x=50, y=200)



    tela_cadastro.mainloop()


# ========================== Tela principal ==============================
def criar_tela_principal():
    # Configurações da janela principal
    tela_main = tk.Tk()
    tela_main.title('Lista telefonica')

    tela_main.config(
        width=400,
        height=400,
        background='#efd147'
    )

    tela_main.resizable(height=False, width=False)


    # Inserir imagem no programa
    imagem = Image.open(r"...\Imagens\titulo_tel.png")
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem = tk.Label(tela_main, image=imagem_tk)
    label_imagem.place(x=50 , y=0 )
    label_imagem.config(
        border=0
    )

    imbot1 = Image.open(r"...\Imagens\cadastrar.png")
    imbot_tk1 = ImageTk.PhotoImage(imbot1)

    imbot2 = Image.open(r"...\Imagens\listacont.png")
    imbot_tk2 = ImageTk.PhotoImage(imbot2)


    # Criando botões na tela principal
    botao1_main = tk.Button(
        text="Cadastrar Novo Contato",
        master=tela_main,
        background="#efd147",
        activebackground="#efd147",
        image=imbot_tk1,
        borderwidth=0,
        command=lambda: abrir_tela_cadastro(tela_main)
    )

    botao2_main = tk.Button(
        text="Ver lista telefonica",
        master=tela_main,
        background="#efd147",
        activebackground="#efd147",
        image=imbot_tk2,
        borderwidth=0,
    )


    botao1_main.place(x=120, y=200)
    botao2_main.place(x=120, y=290)


    tela_main.mainloop()





# ========================== Metodos para navegar ==============================

criar_tela_principal()



