import tkinter as tk
from tkinter import *
from tkinter import simpledialog,messagebox
from PIL import Image, ImageTk

class Tela():
    def __init__(self,master,dicionario,nome,icone) -> None:
        # Definição do toplevel
        if master:
            self.root = tk.Toplevel(master)
        else:
            self.root = tk.Tk()
        
        # Método construtor para os atributos
        self.dict = dicionario
        self.icone = icone

        # Método construtor para definição de tela
        self.root.title(nome)
        self.root.geometry("400x450+500+50")
        self.root.protocol("WM_DELETE_WINDOW",self.fechar)
        self.root.iconbitmap(icone)
        self.root.config(
            background="#fff4ad"
        )

        # Ocultar a janela logo após a criação
        self.root.withdraw()

    def mostrar(self):
        self.root.deiconify()

    def fechar(self):
        # Verifica se a janela Toplevel ainda existe
        if hasattr(self, 'toplevel') and self.toplevel.winfo_exists():
            # Se a janela existir, feche-a
            self.toplevel.destroy()
            self.toplevel = None  # Limpe a referência

        # Verifique se não há mais janelas Toplevel antes de fechar a janela principal
        if not any(isinstance(w, tk.Toplevel) for w in self.root.winfo_children()):
            self.root.destroy()  # Fecha a janela principal
    
    
class Tela_principal(Tela):
    def __init__(self, master, dicionario, nome="Tela principal", icone="ex01_lista_telefonica\\icones\\principal.ico") -> None:
        super().__init__(master, dicionario, nome, icone)


        # Inserindo a imagem na tela principal
        self.imagem_tel_original = Image.open(r"ex01_lista_telefonica\\principais\\tela_principal.png")
        self.imagem_tel_tk = ImageTk.PhotoImage(self.imagem_tel_original)
        self.label_imagem = tk.Label(
            self.root,
            image=self.imagem_tel_tk,
            background="#fff4ad")
        self.label_imagem.place(x=50,y=10)

        # Criando os botões na tela
        # ------- botão cadastrar contato
        self.imagem_botao_cadastrar_original = Image.open(r"ex01_lista_telefonica\\botoes\\botao_cadastrar.png")
        self.imagem_botao_cadastrar_tk = ImageTk.PhotoImage(self.imagem_botao_cadastrar_original)
        self.botao_cadastrar = tk.Button(self.root,image=self.imagem_botao_cadastrar_tk,background="#fff4ad",border=0,activebackground="#fff4ad", command=self.abrir_cadastro)
        self.botao_cadastrar.place(x=100,y=180)

        # -------- botão visualizar lista
        self.imagem_botao_visualizar_original = Image.open(r"ex01_lista_telefonica\\botoes\\botao_visualizar.png")
        self.imagem_botao_visualizar_tk = ImageTk.PhotoImage(self.imagem_botao_visualizar_original)
        self.botao_visualizar = tk.Button(self.root,image=self.imagem_botao_visualizar_tk,background="#fff4ad",border=0,activebackground="#fff4ad", command=self.abrir_lista)
        self.botao_visualizar.place(x=100,y=265)

        # -------- botão visualizar fechar
        self.imagem_botao_fechar_original = Image.open(r"ex01_lista_telefonica\\botoes\\botao_fechar.png")
        self.imagem_botao_fechar_tk = ImageTk.PhotoImage(self.imagem_botao_fechar_original)
        self.botao_fechar = tk.Button(self.root,image=self.imagem_botao_fechar_tk,background="#fff4ad",border=0,activebackground="#fff4ad", command=self.fechar)
        self.botao_fechar.place(x=100,y=350)


    def abrir_cadastro(self):
        self.root.withdraw()
        cadastro = Tela_Cadastro(self.root,self.dict)
        cadastro.mostrar()

    def abrir_lista(self):
        self.root.withdraw()
        lista = Tela_Lista(self.root,self.dict)
        lista.mostrar()


class Tela_Cadastro(Tela):
    def __init__(self, master, dicionario, nome="Tela Cadastro", icone="ex01_lista_telefonica\\icones\\cadastro.ico") -> None:
        super().__init__(master, dicionario, nome, icone)

        
        # Diminuir o tamanho da tela
        self.root.geometry("400x350+500+50")
        # Inserindo a imagem na tela principal
        self.imagem_tel_original = Image.open(r"ex01_lista_telefonica\\principais\\tela_cadastro.png")
        self.imagem_tel_tk = ImageTk.PhotoImage(self.imagem_tel_original)
        self.label_imagem = tk.Label(
            self.root,
            image=self.imagem_tel_tk,
            background="#fff4ad")
        self.label_imagem.place(x=0,y=10)


        # Criar um frame para inserir os dados.
        self.frame = tk.Frame(
            self.root,
            background="white",
            width=390,
            height=120,
            highlightbackground="black",
            highlightthickness=1,
        )
        self.frame.place(x=5,y=80)

        # Colocar os campos para preencher
        # ---------- Labels
        self.lbl_nome = tk.Label(self.root, text="Nome",font=("Arial",20),bg="white")
        self.lbl_tel = tk.Label(self.root,text="Telefone",font=("Arial",20),bg="white")
        self.lbl_nome.place(x=10,y=90)
        self.lbl_tel.place(x=10,y=140)
        # ----------- Entries
        self.ent_nome = tk.Entry(self.root,width=42,bd=3,relief="groove",bg="#faebec")
        self.ent_nome.place(x=130,y=100)
        self.ent_tel = tk.Entry(self.root,width=42,bd=3,relief="groove",bg="#faebec")
        self.ent_tel.place(x=130,y=150)

        # Espaço para colocar os botões
        # ------- botão cadastrar contato
        self.imagem_botao_cadastrar_contato_original = Image.open(r"ex01_lista_telefonica\\botoes\\botao_cadastrar_contato.png")
        self.imagem_botao_cadastrar_contato_tk = ImageTk.PhotoImage(self.imagem_botao_cadastrar_contato_original)
        self.botao_cadastrar_contato = tk.Button(self.root,image=self.imagem_botao_cadastrar_contato_tk,background="#fff4ad",border=0,activebackground="#fff4ad",command=self.cadastrar_contato)
        self.botao_cadastrar_contato.place(x=100,y=215)

        # ------- botão voltar
        self.imagem_botao_voltar_original = Image.open(r"ex01_lista_telefonica\\botoes\\botao_voltar.png")
        self.imagem_botao_voltar_tk = ImageTk.PhotoImage(self.imagem_botao_voltar_original)
        self.botao_voltar = tk.Button(self.root,image=self.imagem_botao_voltar_tk,background="#fff4ad",border=0,activebackground="#fff4ad",command=self.voltar)
        self.botao_voltar.place(x=100,y=285)

    def cadastrar_contato(self):

        # Pegar os valores digitados nos campos e armazenar em variáveis
        nome = self.ent_nome.get().strip()
        tel = self.ent_tel.get().strip()
        self.chave_dict = 0

        # Varrer o dicionário e ver se eles já estão cadastrados

        if nome in self.dict:
            if self.dict[nome] == tel:
                tk.messagebox.showinfo("Erro", f"Contato {nome} já está cadastrado!")
            else:
                tk.messagebox.showinfo("Erro", f"O nome {nome} já está cadastrado com outro telefone!")
        else:
            if nome and tel:
                self.dict[nome] = tel
                self.ent_nome.delete(0,tk.END)
                self.ent_tel.delete(0,tk.END)
                tk.messagebox.showinfo("Sucesso", f"Contato {nome} cadastrado com sucesso!")
            else:
                tk.messagebox.showwarning("Erro", "Preencha todos os campos!")






    def voltar(self):
        principal = Tela_principal(self.root,self.dict)
        principal.mostrar()
        self.root.withdraw()
    

class Tela_Lista(Tela):
    def __init__(self, master, dicionario, nome="Tela Lista", icone="ex01_lista_telefonica\\icones\\lista.ico") -> None:
        super().__init__(master, dicionario, nome, icone)
        
        # Inserindo a imagem na tela principal
        self.imagem_tel_original = Image.open(r"ex01_lista_telefonica\\principais\\lista_de_contatos.png")
        self.imagem_tel_tk = ImageTk.PhotoImage(self.imagem_tel_original)
        self.label_imagem = tk.Label(
            self.root,
            image=self.imagem_tel_tk,
            background="#fff4ad")
        self.label_imagem.place(x=0,y=10)

        # Criar uma listbox + barra de rolagem
        self.listbox = tk.Listbox(
            self.root,
            width=60,
            height=15
        )

        self.rolagem = tk.Scrollbar(self.root, command=self.listbox.yview)
        self.listbox.config(
            yscrollcommand=self.rolagem.set
        )

        self.listbox.place(x=10,y=60)
        self.rolagem.place(x=375, y=60,height=245)

        # Criação dos botões
        # ------- botão pesquisar contato
        self.imagem_botao_pesquisar_contato_original = Image.open(r"ex01_lista_telefonica\\botoes\\pesquisar_contato.png")
        self.imagem_botao_pesquisar_contato_tk = ImageTk.PhotoImage(self.imagem_botao_pesquisar_contato_original)
        self.botao_pesquisar_contato = tk.Button(self.root,image=self.imagem_botao_pesquisar_contato_tk,background="#fff4ad",border=0,activebackground="#fff4ad", command=self.pesquisar)
        self.botao_pesquisar_contato.place(x=20,y=310)

        # ------- botão para deletar
        self.imagem_botao_deletar_contato_original = Image.open(r"ex01_lista_telefonica\\botoes\\deletar_contato.png")
        self.imagem_botao_deletar_contato_tk = ImageTk.PhotoImage(self.imagem_botao_deletar_contato_original)
        self.botao_deletar_contato = tk.Button(self.root,image=self.imagem_botao_deletar_contato_tk,background="#fff4ad",border=0,activebackground="#fff4ad",command=self.deletar_contato)
        self.botao_deletar_contato.place(x=200,y=310)

        # ------- botão voltar
        self.imagem_botao_voltar_original = Image.open(r"ex01_lista_telefonica\\botoes\\botao_voltar.png")
        self.imagem_botao_voltar_tk = ImageTk.PhotoImage(self.imagem_botao_voltar_original)
        self.botao_voltar = tk.Button(self.root,image=self.imagem_botao_voltar_tk,background="#fff4ad",border=0,activebackground="#fff4ad", command=self.voltar)
        self.botao_voltar.place(x=100,y=380)

        self.carregar_contatos()

    def carregar_contatos(self):
        """Carrega os contatos na listbox."""
        self.listbox.delete(0, tk.END)
        for nome, telefone in self.dict.items():
            self.listbox.insert(tk.END, f"{nome}: {telefone}")

    def deletar_contato(self):
        selecionado = self.listbox.curselection()

        if selecionado:
            contato = self.listbox.get(selecionado)
            nome_contato = contato.split(":")[0].strip()
            if nome_contato in self.dict:
                del self.dict[nome_contato]
                tk.messagebox.showinfo("Sucesso",f"Contato {nome_contato} deletado com sucesso!")
            self.carregar_contatos()
        else:
            tk.messagebox.showinfo("Erro","Nenhum contato selecionado para deletar")

    def pesquisar(self):
        pesquisar = Tela_pesquisa(self.root,self.dict)
        pesquisar.mostrar()
        self.root.withdraw()

    def voltar(self):
        principal = Tela_principal(self.root,self.dict)
        principal.mostrar()
        self.root.withdraw()


class Tela_pesquisa(Tela):
    def __init__(self, master, dicionario, nome="Tela de Pesquisa", icone=r"ex01_lista_telefonica\\icones\\pesquisa.ico") -> None:
        super().__init__(master, dicionario, nome, icone)

        
        # Inserindo a imagem na tela principal
        self.imagem_tel_original = Image.open(r"ex01_lista_telefonica\\principais\\pesquisar_contato.png")
        self.imagem_tel_tk = ImageTk.PhotoImage(self.imagem_tel_original)
        self.label_imagem = tk.Label(
            self.root,
            image=self.imagem_tel_tk,
            background="#fff4ad")
        self.label_imagem.place(x=0,y=10)
        
        # Criação da label para pesquisa
        self.lbl_nome = tk.Label(self.root, text="Nome",font=("Arial",20),bg="#fff4ad")
        self.lbl_nome.place(x=30,y=90)
        self.ent_nome = tk.Entry(self.root,width=42,bd=3,relief="groove",bg="#faebec")
        self.ent_nome.place(x=110,y=100)

        # Criação dos botões
        # ------- botão pesquisar contato
        self.imagem_botao_pesquisar_contato_original = Image.open(r"ex01_lista_telefonica\\botoes\\pesquisar_contato.png")
        self.imagem_botao_pesquisar_contato_tk = ImageTk.PhotoImage(self.imagem_botao_pesquisar_contato_original)
        self.botao_pesquisar_contato = tk.Button(self.root,image=self.imagem_botao_pesquisar_contato_tk,background="#fff4ad",border=0,activebackground="#fff4ad",command=self.pesquisar_contato)
        self.botao_pesquisar_contato.place(x=20,y=150)

        # ------- botão para deletar
        self.imagem_botao_deletar_contato_original = Image.open(r"ex01_lista_telefonica\\botoes\\deletar_contato.png")
        self.imagem_botao_deletar_contato_tk = ImageTk.PhotoImage(self.imagem_botao_deletar_contato_original)
        self.botao_deletar_contato = tk.Button(self.root,image=self.imagem_botao_deletar_contato_tk,background="#fff4ad",border=0,activebackground="#fff4ad",command=self.deletar_contato)
        self.botao_deletar_contato.place(x=200,y=150)

        # ------- botão voltar
        self.imagem_botao_voltar_original = Image.open(r"ex01_lista_telefonica\\botoes\\botao_voltar.png")
        self.imagem_botao_voltar_tk = ImageTk.PhotoImage(self.imagem_botao_voltar_original)
        self.botao_voltar = tk.Button(self.root,image=self.imagem_botao_voltar_tk,background="#fff4ad",border=0,activebackground="#fff4ad", command=self.voltar)
        self.botao_voltar.place(x=100,y=340)

        # Criar um frame para mostrar os dados.
        self.frame = tk.Frame(
            self.root,
            background="white",
            width=390,
            height=50,
            highlightbackground="black",
            highlightthickness=1,
        )
        self.frame.place(x=5,y=250)
        self.lbl_resultado = tk.Label(self.frame, text="", font=("Arial", 20), fg="black",bg="white")
        self.lbl_resultado.place(x=5,y=5)

    def pesquisar_contato(self):
        nome = self.ent_nome.get().strip()
        if nome in self.dict:
            telefone = self.dict[nome]
            self.lbl_resultado.config(text=telefone)
            self.contato_encontrado = nome  # Armazena o contato encontrado
        else:
            tk.messagebox.showwarning("Erro", "Contato não localizado!")
            self.lbl_resultado.config(text="")
            self.contato_encontrado = None  # Limpa se não encontrado

    def deletar_contato(self):
        if self.contato_encontrado:  # Verifica se um contato foi encontrado
            del self.dict[self.contato_encontrado]
            messagebox.showinfo("Sucesso", f"Contato '{self.contato_encontrado}' deletado com sucesso!")
            self.lbl_resultado.config(text="")
            self.contato_encontrado = None  # Limpa após deletar
        else:
            messagebox.showwarning("Atenção", "Pesquise um contato antes de deletar.")


    def voltar(self):
        lista = Tela_Lista(self.root, self.dict)
        lista.mostrar()
        self.root.withdraw()
        

# Iniciando o programa

# ------ dicionário global a ser usado
contatos = {}

# ------ iniciando programa
root = tk.Tk()
root.title("Janela principal oculta")
root.withdraw()

janela_principal = Tela_principal(root, contatos)
janela_principal.mostrar()

root.mainloop()
