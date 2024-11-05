def contar_vogais():
    entrada = input("Digite uma string: ")
    vogais = "aeiouAEIOU"
    quantidade_vogais = sum(1 for char in entrada if char in vogais)
    print(f"Quantidade de vogais: {quantidade_vogais}")
    print("String original:", entrada)

contar_vogais()
