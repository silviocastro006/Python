import tkinter as tk
from tkinter import messagebox,simpledialog
from PIL import Image, ImageTk

class Tela:
    def __init__(self,master,nome,icone) -> None:
        
        # definição do toplevel
        if master:
            self.root = tk.Toplevel(master)
        else:
            self.root = tk.Tk()

        # Criação dos atributos de cada tela
        self.root.title(nome)
        self.root.iconbitmap(icone)

        # Método construtor para definição de tela
        self.root.geometry("510x550+500+50")
        self.root.protocol("WM_DELETE_WINDOW",self.fechar)
        self.root.config(background="#cee0d9")
        self.root.resizable(False,False)

        # Ocultar a janela logo após a criação
        self.root.withdraw()

    def criar_botao(self,caminhoImg, comando=None, x=0,y=0):
        imagem_original = Image.open(caminhoImg)
        imagem_tk = ImageTk.PhotoImage(imagem_original)
        botao = tk.Button(self.root,image=imagem_tk,background="#cee0d9", border=0,activebackground="#cee0d9",command=comando)
        botao.image = imagem_tk
        botao.place(x=x,y=y)
        return botao
    
    def criar_banner(self,caminhoImg,largura=0,altura=0, x=0,y=0):
        imagem_original = Image.open(caminhoImg)
        imagem_tk = ImageTk.PhotoImage(imagem_original)
        banner = tk.Label(self.root,image = imagem_tk,background="#cee0d9",width=largura,height=altura)
        banner.image = imagem_tk
        banner.place(x=x,y=y)
        return banner
    
    def criar_label(self,texto=None,tamanho=0,x=0,y=0):
        label = tk.Label(self.root,text=texto,font=("Arial",tamanho),bg="white")
        label.place(x=x,y=y)
        return label
    
    def criar_frame(self,largura=0, altura=0,x=0,y=0):
        frame = tk.Frame(self.root,width=largura,height=altura,background="white", highlightbackground="black",highlightthickness=1).place(x=x,y=y)
        return frame

    def criar_input(self, largura=0,x=0, y=0):
        entrada = tk.Entry(self.root, font=("Arial",15),width=largura,relief="groove",bg="#f0f0f0",highlightbackground="black",highlightthickness=1).place(x=x,y=y)

    def mostrar(self):
        self.root.deiconify()


    def fechar(self):
        if hasattr(self,"toplevel") and self.toplevel.winfo_exists():
            self.toplevel.destroy()
            self.toplevel = None

        if not any(isinstance(w,tk.Toplevel) for w in self.root.winfo_children()):
            self.root.destroy()


class Tela_principal(Tela):
    def __init__(self, master, nome="Tela Inicial", icone=None) -> None:
        super().__init__(master, nome, icone)

        # alterando o tamanho, a tela está um pouco grande
        self.root.geometry("510x500+500+50")

        # Inserindo imagem na tela principal
        self.banner = self.criar_banner("ex02_oficina_veiculos\\principal\\tela_inicial.png",300,200,105,20)

        # Inserindo os botões na tela
        # --------- Cadastrar Veiculo
        self.botao_cadastrar = self.criar_botao(caminhoImg="ex02_oficina_veiculos\\botoes\\Tela_veiculo.png",x=30,y=260)
        # --------- Cadastrar Serviço
        self.botao_servico = self.criar_botao(caminhoImg="ex02_oficina_veiculos\\botoes\\Tela_Serviço.png", x=280, y=260)
        # --------- Controle de Serviços
        self.botao_controle = self.criar_botao(caminhoImg="ex02_oficina_veiculos\\botoes\\tela_controle.png",x=30,y=380)
        # --------- Fechar o programa
        self.botao_fechar = self.criar_botao(caminhoImg="ex02_oficina_veiculos\\botoes\\fechar_programa.png",x=280,y=380,comando=self.fechar)
    
class Tela_cadastro_veiculo(Tela):
    def __init__(self, master, nome="Cadastro de Veículo", icone=None) -> None:
        super().__init__(master, nome, icone)

        # Alterar o tamanho da tela
        self.root.geometry("510x560+500+50")

        # Inserindo imagem na tela principal
        self.banner = self.criar_banner("ex02_oficina_veiculos\\principal\\titulo_cadastro_veiculo.png",400,50,55,8)

        # inserindo um frame para os dados]
        self.frame_cadas = self.criar_frame(490,320,10,70)

        # Criando os labels para os cadastros
        self.lbl_nome = self.criar_label(texto="Nome do cliente",tamanho=15,x=20,y=90)

        self.lbl_contato = self.criar_label(texto="Contato do cliente",tamanho=15,x=20,y=140)

        self.lbl_tipo = self.criar_label(texto="Tipo do veículo",tamanho=15,x=20,y=190)

        self.lbl_placa = self.criar_label(texto="Placa do veículo",tamanho=15,x=20,y=240)

        self.lbl_cor = self.criar_label(texto="Cor do veículo",tamanho=15,x=20,y=290)

        self.lbl_marca = self.criar_label(texto="Marca do Veículo",tamanho=15,x=20,y=340)

        # Criando os inputs para os cadastros
        self.ent_nome = self.criar_input(26,195,90)

        self.ent_contato = self.criar_input(26,195,140)

        self.ent_tipo = self.criar_input(26,195,190)

        self.ent_placa = self.criar_input(26,195,240)

        self.ent_cor = self.criar_input(26,195,290)

        self.ent_marca = self.criar_input(26,195,340)

        # Criar os botões do menu
        # ------ Cadastrar veículo
        self.botao_cadastrar_veiculo = self.criar_botao(caminhoImg="ex02_oficina_veiculos\\botoes\\cadastro_veic.png",x=30,y=405)

        # ------ Pesquisar veículo
        self.pesquisar_veiculo = self.criar_botao(caminhoImg="ex02_oficina_veiculos\\botoes\\pesquisa_veic.png",x=280,y=405)


        # ------ Voltar à tela anterior
        self.botao_voltar = self.criar_botao("ex02_oficina_veiculos\\botoes\\voltar_tela.png",x=155,y=480)























root = tk.Tk()
root.withdraw()

cadastro_veiculo = Tela_cadastro_veiculo(root)
cadastro_veiculo.mostrar()

root.mainloop()