# 1 - Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O número {numero} é Par')
    else:
        print(f'O número {numero} é Impar')
except:
    try:
        numero = float(numero)
        print(f'O número é quase certo, mas infelizmente é {type(numero)}')
    except:
        print(f'Numero digitado não é inteiro ele é do tipo: {type(numero)}')

# Soluçao do professor

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'
    if par_impar:
        par_impar_texto = 'par'
    print(f'O numéro digitado é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')