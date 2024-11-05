import os

class Usuario:
    def __init__(self, nome, sexo, idade, altura) -> None:
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.altura = altura

    def to_string(self):
        return f"{self.nome};{self.sexo};{self.idade};{self.altura}"

    @staticmethod
    def from_string(data_str):
        nome, sexo, idade, altura = data_str.strip().split(";")
        return Usuario(nome, sexo, int(idade), float(altura))


class Lista:
    def __init__(self, arquivo) -> None:
        self.lista_usuarios = list()
        self.arquivo = arquivo
        self.carregar_usuarios()

    def carregar_usuarios(self):
        try:
            with open(self.arquivo, "r") as file:
                for line in file:
                    usuario = Usuario.from_string(line)
                    self.lista_usuarios.append(usuario)
        except FileNotFoundError:
            with open(self.arquivo, "w") as file:
                pass  # Cria o arquivo se não existir

    def salvar_usuario(self, usuario):
        with open(self.arquivo, "a") as file:
            file.write(usuario.to_string() + "\n")

    def atualizar_arquivo(self):
        with open(self.arquivo, "w") as file:
            for usuario in self.lista_usuarios:
                file.write(usuario.to_string() + "\n")

    def adicionar_usuario(self, usuario):
        self.lista_usuarios.append(usuario)
        self.salvar_usuario(usuario)
        print(f"Usuário {usuario.nome} adicionado com sucesso.")

    def deletar_usuario(self, nome_usuario):
        for usuario in self.lista_usuarios:
            if usuario.nome == nome_usuario:
                self.lista_usuarios.remove(usuario)
                self.atualizar_arquivo()
                print(f"Usuário {nome_usuario} deletado com sucesso!")
                return
        print("Não existe usuário com esse nome.")

    def listar_usuarios(self):
        print("========= Listando usuários ========")
        for usuario in self.lista_usuarios:
            print(f"Nome: {usuario.nome}\nSexo: {usuario.sexo}\nIdade: {usuario.idade}\nAltura: {usuario.altura}")
            print("-" * 40)


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# Programa principal
lista_users = Lista("usuarios.txt")

while True:
    print("===== Menu de Opções ======")
    print("1) Criar usuário")
    print("2) Listar usuários")
    print("3) Deletar usuário")
    print("4) Finalizar programa")

    escolha = input("Opção desejada: ")
    if escolha == "1":
        limpar()
        nome = input("Digite um nome: ")
        sexo = input("Escolha um sexo: ")
        idade = int(input("Insira a idade: "))
        altura = float(input("Insira a altura em metros: "))
        user = Usuario(nome, sexo, idade, altura)
        lista_users.adicionar_usuario(user)
        input("Aperte qualquer tecla para continuar...")
        limpar()

    elif escolha == "2":
        limpar()
        lista_users.listar_usuarios()
        input("Aperte qualquer tecla para continuar...")
        limpar()

    elif escolha == "3":
        limpar()
        lista_users.listar_usuarios()
        nome_usuario = input("Digite o nome do usuário a ser deletado: ")
        lista_users.deletar_usuario(nome_usuario)
        input("Aperte qualquer tecla para continuar...")
        limpar()

    elif escolha == "4":
        limpar()
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
