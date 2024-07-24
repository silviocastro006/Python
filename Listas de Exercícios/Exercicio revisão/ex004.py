# 4 – Faça um programa que gere um vetor de 10 posições para números inteiros,
# preencha o vetor com números diversos, organize o vetor do menor para o maior e
# mostre:
# a) O vetor digitado originalmente;
# b) O vetor organizado do menor para o maior;

vetor = list()

for c in range(10):
    n = int(input('Valor: '))
    vetor.append(n)

print(f'O Vetor original de 10 posições foi: {vetor}')
print(f'O Vetor organizado do menor para o maior é: {sorted(vetor)}')