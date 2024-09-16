from random import randint # importo a função randint da biblioteca random

# crio uma matriz com valores aleatório de 0 a 10
matriz = [[randint(0,10),randint(0,10),randint(0,10)],[randint(0,10),randint(0,10),randint(0,10)],[randint(0,10),randint(0,10),randint(0,10)]]

# criação de uma função com o nome de maior, ela vai determinar o maior número dentro de uma lista
def maior():
    contador = 0
    maior = 0
    for lista in matriz:
        for numero in lista:
            if contador == 0:
                maior = numero
            if numero > maior:
                maior = numero
    return maior

# criação de uma função com o nome de média, ela vai determinar a média dos números em uma lista
def media():
    total = 0
    contador = 0
    for lista in matriz:
        for numero in lista:
            total += numero
    media = total/9
    return media

# criação de uma função com o nome de organizar, ela vai organizar numericamente os valores na lista
def organizar():
    global matriz
    temporaria = list()
    organizada = list()
    
    for lista in matriz:
        for numero in lista:
            temporaria.append(numero)
    temporaria.sort()
    
    for c in range(3):
        organizada.append([])

    posicao = 0
    indice = 0

    for lista in organizada:
        for numero in range(3):
            organizada[indice].append(temporaria[posicao])
            posicao+=1
        indice+=1

    return organizada
    

# os resultados das funções são armazenados em variáveis
maior_num = maior()
media_val = media()
organizado = organizar()

# mostrar o resultado no console
print(f'A matriz digitada originalmente é {matriz}')
print(f'O maior valor da matriz é {maior_num}')
print(f'A matriz organizada do menor para o maior é {organizado}')
print(f'A media dos valores é {media_val:.2f}')



