class Termo:
    def __init__(self, nome):
        self.nome = nome
        self.descricoes = []

    def adicionar_descricao(self, descricao):
        self.descricoes.append(descricao)

    def listar_descricoes(self):
        return self.descricoes


class Dicionario:
    def __init__(self):
        self.termos = {}

    def adicionar_termo(self, nome, descricao):
        if nome in self.termos:
            self.termos[nome].adicionar_descricao(descricao)
        else:
            novo_termo = Termo(nome)
            novo_termo.adicionar_descricao(descricao)
            self.termos[nome] = novo_termo

    def buscar_termo(self, termo_busca):
        for nome in self.termos.keys():
            if self.similaridade(nome, termo_busca) >= 0.7:
                print(f"Termo encontrado: {nome}")
                for descricao in self.termos[nome].listar_descricoes():
                    print(f"- {descricao}")

    @staticmethod
    def similaridade(str1, str2):
        len_str1 = len(str1)
        len_str2 = len(str2)
        if len_str1 == 0: return len_str2
        if len_str2 == 0: return len_str1
        
        distancia = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]
        for i in range(len_str1 + 1):
            distancia[i][0] = i
        for j in range(len_str2 + 1):
            distancia[0][j] = j
        
        for i in range(1, len_str1 + 1):
            for j in range(1, len_str2 + 1):
                custo = 0 if str1[i - 1] == str2[j - 1] else 1
                distancia[i][j] = min(
                    distancia[i - 1][j] + 1,
                    distancia[i][j - 1] + 1, 
                    distancia[i - 1][j - 1] + custo
                )

        distancia_maxima = max(len_str1, len_str2)
        return 1 - (distancia[len_str1][len_str2] / distancia_maxima) 



dicionario = Dicionario()

while True:
    print("\n===== Menu de Opções =====")
    print("1) Adicionar Termo e Descrição")
    print("2) Buscar Termo")
    print("3) Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o termo: ")
        descricao = input("Digite a descrição: ")
        dicionario.adicionar_termo(nome, descricao)
        print(f'Termo "{nome}" adicionado com a descrição.')

    elif escolha == "2":
        termo_busca = input("Digite o termo que deseja buscar: ")
        dicionario.buscar_termo(termo_busca)

    elif escolha == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
