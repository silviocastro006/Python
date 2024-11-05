def contar_palavras():
    entrada = input("Digite uma frase: ")
    palavras = entrada.split() 
    quantidade_palavras = len(palavras)
    print("Número de palavras:", quantidade_palavras)

contar_palavras()
