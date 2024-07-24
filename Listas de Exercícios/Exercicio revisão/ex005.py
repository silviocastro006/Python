# 5 - Faça um programa que gere uma matriz de 3 x 3, que receba números aleatórios,
# organize esta matriz do maior para o menor e mostre: ----> ok
# a) A matriz digitada originalmente; ---------------------> ok
# b) A matriz organizada do menor para o maior; ?
# c) O maior valor da matriz; -----------------------------> ok
# d) A média dos números digitados na matriz

from random import randint

matriz = [[randint(0,10),randint(0,10),randint(0,10)],[randint(0,10),randint(0,10),randint(0,10)],[randint(0,10),randint(0,10),randint(0,10)]]


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

def media():
    total = 0
    contador = 0
    for lista in matriz:
        for numero in lista:
            total += numero
    media = total/9
    return media

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
    


maior_num = maior()
media_val = media()
organizado = organizar()

print(f'A matriz digitada originalmente é {matriz}')
print(f'O maior valor da matriz é {maior_num}')
print(f'A matriz organizada do menor para o maior é {organizado}')
print(f'A media dos valores é {media_val:.2f}')



