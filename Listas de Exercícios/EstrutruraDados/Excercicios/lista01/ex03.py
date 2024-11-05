import os

class Pessoa:
    def __init__(self, nome, cpf, rg, email, endereco) -> None:
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.email = email
        self.endereco = endereco

    def to_string(self):
        return f"{self.nome};{self.cpf};{self.rg};{self.email};{self.endereco}"

    @staticmethod
    def from_string(data_str):
        nome, cpf, rg, email, endereco = data_str.strip().split(";")
        return Pessoa(nome, cpf, rg, email, endereco)


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

    def buscar_por_cpf(self, cpf):
        for pessoa in self.lista_pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        return None

    def listar_pessoas(self):
        print("========= Listando pessoas ========")
        for pessoa in self.lista_pessoas:
            print(f"Nome: {pessoa.nome}\nCPF: {pessoa.cpf}\nRG: {pessoa.rg}\nEmail: {pessoa.email}\nEndereço: {pessoa.endereco}")
            print("-" * 40)


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# Programa principal
cadastro_pessoas = Cadastro("pessoas.txt")

while True:
    print("===== Menu de Opções ======")
    print("1) Inserir dados de uma pessoa")
    print("2) Buscar pessoa por CPF")
    print("3) Listar todas as pessoas cadastradas")
    print("4) Finalizar programa")

    escolha = input("Opção desejada: ")
    if escolha == "1":
        limpar()
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        rg = input("Digite o RG: ")
        email = input("Digite o e-mail: ")
        endereco = input("Digite o endereço: ")
        pessoa = Pessoa(nome, cpf, rg, email, endereco)
        cadastro_pessoas.adicionar_pessoa(pessoa)
        input("Aperte qualquer tecla para continuar...")
        limpar()

    elif escolha == "2":
        limpar()
        cpf_busca = input("Digite o CPF da pessoa que deseja buscar: ")
        pessoa_encontrada = cadastro_pessoas.buscar_por_cpf(cpf_busca)
        if pessoa_encontrada:
            print("========= Pessoa Encontrada ========")
            print(f"Nome: {pessoa_encontrada.nome}\nCPF: {pessoa_encontrada.cpf}\nRG: {pessoa_encontrada.rg}\nEmail: {pessoa_encontrada.email}\nEndereço: {pessoa_encontrada.endereco}")
        else:
            print("Pessoa não encontrada.")
        input("Aperte qualquer tecla para continuar...")
        limpar()

    elif escolha == "3":
        limpar()
        cadastro_pessoas.listar_pessoas()
        input("Aperte qualquer tecla para continuar...")
        limpar()

    elif escolha == "4":
        limpar()
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
