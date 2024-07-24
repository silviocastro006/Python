# 2 – Faça um programa que leia o nome, idade e sexo de várias pessoas até que o nome
# digitado seja “FIM” e informe: -----------------> ok
# a) O nome e a idade da pessoa mais velha; ------> ok
# b) O nome e a idade da pessoa mais nova; --------> ok
# c) Quantas pessoas eram do sexo masculino; -------> ok
# d) Quantas pessoas eram do sexo feminino; --------> ok
# e) A quantidade de pessoas digitadas e a média de idade. ------> ok

maior_idade = menor_idade = contador = quantidade_masc = quantidade_fem = tot_idade = 0
nome_velho = nome_novo = ''

while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M] ou [F]: ')[0].upper()
    while sexo not in 'MF':
        sexo = input('Digite um valor válido para Sexo [M] ou [F]: ')[0].upper()
       
    if contador == 0:
        maior_idade = idade # --------> iniciar as variáveis mais velhas
        nome_velho = nome
        menor_idade = idade
        nome_novo = nome

    if idade > maior_idade:
        maior_idade = idade # ---------> atualizar os valores dos mais velhos
        nome_velho = nome

    if idade < menor_idade:
        menor_idade = idade # ----------> atualizar os valores dos mais novos
        nome_novo = nome

    if sexo == 'M':
        quantidade_masc += 1 # ---------> atualizar quantidade de sexo masculino
    else:
        quantidade_fem += 1  # ---------> atualizar quantidade de sexo feminino

    tot_idade += idade       # ----------> valor total de idade
    contador += 1            # ----------> atualização do contador

    resp = input('Digite FIM para terminar: ').upper()
    if resp == 'FIM':
        break
    print('-'*30)
print('-'*30)
media = tot_idade/contador

print(f'A pessoa mais velha se chama {nome_velho} com {maior_idade} anos')
print(f'A pessoa mais nova se chama {nome_novo} com {menor_idade} anos')
print(f'Foram no total {quantidade_masc} pessoas do sexo MASCULINO')
print(f'Foram no total {quantidade_fem} pessoas do sexo FEMININO')
print(f'Totalizaram {contador} pessoas com uma média de idade de {media:.2f} anos')
