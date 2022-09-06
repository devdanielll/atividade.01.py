# Faça um programa que leia 5 números e informe a soma e a média dos números.

from statistics import mean

numeros = []

for i in range(5):
    numeros.append(int(input("Digite um número: ")))

soma_numeros = sum(numeros)
media_numeros = mean(numeros)
print(f'A soma dos números digitados é {soma_numeros}')
print(f'A média dos números digitados é: {media_numeros}')