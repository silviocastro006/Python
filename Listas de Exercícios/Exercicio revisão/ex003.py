# 3 – Faça um programa que leia o número e o peso de um boi, a leitura encerra quando o
# número digitado for 0 (zero) e informe: -------> ok
# a) Quantos bois foram digitados; --------------> ok
# b) Qual o total de peso dos bois; -------------> ok
# c) Qual a média de peso dos bois; --------------> ok
# d) Qual o número e o peso do boi mais pesado;  --> ok
# e) Qual o número e o peso do boi mais leve. ------> ok


continua =  True
contador = tot_peso = mais_pesado = mais_leve = num_pesado = num_leve = 0

while True:
    numero = int(input('Numero do Boi: '))
    if numero == 0:
        break
    peso = float(input('Peso do Boi @: '))
    

    if contador == 0:
        num_pesado = numero # -------------------------> iniciando as variáveis para comparar
        mais_pesado = peso
        num_leve = numero
        mais_leve = peso

    if peso > mais_pesado:
        mais_pesado = peso  # -------------------------> atualizando os mais pesados
        num_pesado = numero
    
    if peso < mais_leve:
        mais_leve = peso    # -------------------------> atualizando os mais leves
        num_leve = numero

    
    contador += 1
    tot_peso += peso
    print('-'*30)
print('-'*30)
media = tot_peso/contador

print(f'No total foram digitados {contador} Bois')
print(f'O peso total dos Bois é de {tot_peso} @')
print(f'A média de peso foi de {media} @')
print(f'O Boi mais pesado foi o número {num_pesado} com {mais_pesado} @')
print(f'O Boi mais leve foi o número {num_leve} com {mais_leve} @')