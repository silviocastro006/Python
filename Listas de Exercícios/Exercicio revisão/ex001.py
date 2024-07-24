# 1 - Faça um programa que leia 10 números e informe: 0k
# a) A soma destes números; ok
# b) A média destes números; ok
# c) O maior número; ok
# d) O menor número

soma = maior = menor = 0


for n in range(10):
    numero = int(input('Digite um número: '))
    soma += numero
    if n == 0:
        maior = numero
        menor = numero

    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero

media = soma/10

print(f'A soma total dos valores é: {soma}')
print(f'A média dos valores é {media}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')

