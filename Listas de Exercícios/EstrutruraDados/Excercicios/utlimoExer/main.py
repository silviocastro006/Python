import datetime
import os

class Cliente:
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.historico_compras = []

class Produto:
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco

class Venda:
    def __init__(self, cliente, itens):
        self.data = datetime.datetime.now()
        self.cliente = cliente
        self.itens = itens
        self.valor_total = sum(item.preco for item in itens)
        cliente.historico_compras.append(self)

    def __str__(self):
        return (f"Data: {self.data}\n"
                f"Cliente: {self.cliente.nome}\n"
                f"Itens: {', '.join([item.descricao for item in self.itens])}\n"
                f"Valor Total: R$ {self.valor_total:.2f}")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_cliente(clientes):
    limpar_tela()
    print("Cadastro de Cliente")
    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    telefone = input("Telefone do cliente: ")
    email = input("Email do cliente: ")
    clientes.append(Cliente(nome, cpf, telefone, email))
    print("Cliente cadastrado com sucesso!")

def registrar_venda(clientes, vendas):
    limpar_tela()
    if not clientes:
        print("Não há clientes cadastrados. Cadastre um cliente antes de registrar uma venda.")
        return
    
    listar_clientes(clientes)
    cliente_idx = int(input("Selecione o número do cliente: ")) - 1

    if cliente_idx < 0 or cliente_idx >= len(clientes):
        print("Cliente inválido.")
        return

    cliente = clientes[cliente_idx]
    itens = []

    while True:
        descricao = input("Descrição do produto (ou 'sair' para finalizar): ")
        if descricao.lower() == 'sair':
            break
        preco = float(input("Preço do produto: "))
        itens.append(Produto(descricao, preco))

    if itens:
        venda = Venda(cliente, itens)
        vendas.append(venda)
        print("Venda registrada com sucesso!")
        print(venda)
        
    else:
        print("Nenhum item foi adicionado à venda.")

def listar_clientes(clientes):
    limpar_tela()
    print("Lista de Clientes")
    if not clientes:
        print("Não há clientes cadastrados.")
    else:
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i}. {cliente.nome} - {cliente.cpf}")

def consultar_vendas(vendas):
    limpar_tela()
    print("Consulta de Vendas")
    if not vendas:
        print("Não há vendas registradas.")
    else:
        for i, venda in enumerate(vendas, start=1):
            print(f"\nVenda {i}")
            print(venda)

def main():
    clientes = []
    vendas = []

    while True:
        limpar_tela()
        print("Menu:")
        print("1. Cadastrar cliente")
        print("2. Registrar venda")
        print("3. Listar clientes")
        print("4. Consultar vendas")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente(clientes)
        elif opcao == '2':
            registrar_venda(clientes, vendas)
        elif opcao == '3':
            listar_clientes(clientes)
            input("\nPressione Enter para voltar ao menu.")
        elif opcao == '4':
            consultar_vendas(vendas)
            input("\nPressione Enter para voltar ao menu.")
        elif opcao == '5':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
