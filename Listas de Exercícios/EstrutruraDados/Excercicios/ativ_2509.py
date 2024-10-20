"""
Crie um programa que deverá controlar os dados de "n" pessoas conforme as características e funcionalidade listadas abaixo:

-Registar o nome, telefone, e-mail e cpf e cada pessoa(utilize um dicionário para executar essa operação)
-O programa deverá exibir um menu para que o usuário fique informado sobre as operações existentes no programa;
-Opção para inserir os dados de uma pessoa
-Opção para listar os dados de todas as pessoas
-Sair do programa( e gravar os dados que estão contidos na lista de dados)
-Atenção: O programa deve carregar os dados contidos no arquivo de "memória" ao ser inicializado. 

"""
class DicionarioPessoas:
    def __init__(self):
        # Carrega os dados do arquivo se existir, senão cria uma lista vazia
        self.lista_pessoas = self.carregar_dados()

    def cadastrar_pessoa(self, nome, telefone, email, cpf):
        # Cria um dicionário com os dados da pessoa
        pessoa = {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "cpf": cpf
        }
        # Adiciona o dicionário na lista
        self.lista_pessoas.append(pessoa)

    def listar_pessoas(self):
        if not self.lista_pessoas:
            print("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in self.lista_pessoas:
                print(f"Nome: {pessoa['nome']}")
                print(f"Telefone: {pessoa['telefone']}")
                print(f"Email: {pessoa['email']}")
                print(f"CPF: {pessoa['cpf']}")
                print("-" * 30)

    def carregar_dados(self):
        lista = []
        try:
            with open("pessoas_lista.txt", "r") as file:
                for linha in file:
                    # Cada linha será lida e convertida em um dicionário
                    dados = linha.strip().split(", ")
                    pessoa = {
                        "nome": dados[0],
                        "telefone": dados[1],
                        "email": dados[2],
                        "cpf": dados[3]
                    }
                    lista.append(pessoa)
        except FileNotFoundError:
            # Se o arquivo não existir, retorna uma lista vazia
            return lista
        return lista

    def salvar_dados(self):
        with open("pessoas_lista.txt", "w") as file:
            for pessoa in self.lista_pessoas:
                # Escreve cada pessoa no arquivo em uma linha separada
                file.write(f"{pessoa['nome']}, {pessoa['telefone']}, {pessoa['email']}, {pessoa['cpf']}\n")


def exibir_menu():
    print("\nMenu:")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Sair")


def main():
    dicionario = DicionarioPessoas()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            cpf = input("Digite o CPF: ")
            dicionario.cadastrar_pessoa(nome, telefone, email, cpf)
            print("Pessoa cadastrada com sucesso!")

        elif opcao == "2":
            dicionario.listar_pessoas()

        elif opcao == "3":
            dicionario.salvar_dados()
            print("Dados salvos em 'pessoas_lista.txt'. Saindo do programa...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
