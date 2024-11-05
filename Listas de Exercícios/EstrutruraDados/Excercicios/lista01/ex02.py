import os

class Pessoa:
    def __init__(self, nome, cpf, rg, email) -> None:
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.email = email

    def to_string(self):
        return f"{self.nome};{self.cpf};{self.rg};{self.email}"

    @staticmethod
    def from_string(data_str):
        nome, cpf, rg, email = data_str.strip().split(";")
        return Pessoa(nome, cpf, rg, email)


class Cadastro:
    def __init__(self, arquivo) -> None:
        self.lista_pessoas = list()
        self.arquivo = arquivo
        self.carregar_pessoas()

    def carregar_pessoas(self):
        try:
            with open(self.arquivo, "r") as file:
                for line in file:
                    pessoa = Pessoa.from_string(line)
                    self.lista_pessoas.append(pessoa)
        except FileNotFoundError:
            with open(self.arquivo, "w") as file:
                pass  # Cria o arquivo se não existir

    def salvar_pessoa(self, pessoa):
        with open(self.arquivo, "a") as file:
            file.write(pessoa.to_string() + "\n")

    def atualizar_arquivo(self):
        with open(self.arquivo, "w") as file:
            for pessoa in self.lista_pessoas:
                file.write(pessoa.to_string() + "\n")

    def adicionar_pessoa(self, pessoa):
        self.lista_pessoas.append(pessoa)
        self.salvar_pessoa(pessoa)
        print(f"Pessoa {pessoa.nome} cadastrada com sucesso.")

    def listar_pessoas(self):
        print("========= Listando pessoas ========")
        for pessoa in self.lista_pessoas:
            print(f"Nome: {pessoa.nome}\nCPF: {pessoa.cpf}\nRG: {pessoa.rg}\nEmail: {pessoa.email}")
            print("-" * 40)


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# Programa principal
cadastro_pessoas = Cadastro("pessoas.txt")

while True:
    print("===== Menu de Opções ======")
    print("1) Inserir dados de uma pessoa")
    print("2) Listar todas as pessoas cadastradas")
    print("3) Finalizar programa")

    escolha = input("Opção desejada: ")
    if escolha == "1":
        limpar()
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        rg = input("Digite o RG: ")
        email = input("Digite o e-mail: ")
        pessoa = Pessoa(nome, cpf, rg, email)
        cadastro_pessoas.adicionar_pessoa(pessoa)
        input("Aperte qualquer tecla para continuar...")
        limpar()

    elif escolha == "2":
        limpar()
        cadastro_pessoas.listar_pessoas()
        input("Aperte qualquer tecla para continuar...")
        limpar()

    elif escolha == "3":
        limpar()
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
