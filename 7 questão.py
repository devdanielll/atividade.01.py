# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

from math import inf

maior = -inf
menor = inf

soma = 0
contador = 0
print("Para parar digite -700")
while True:
    temp = float(input("Digite a temperatura: "))
    if temp == -700:
        break

    contador += 1
    soma += temp
    if temp < menor:
        menor = temp
    if temp > maior:
        maior = temp

print(f"A menor temperatura foi: {menor}")
print(f"A maior temperatura foi: {maior}")
print(f"A média das temperaturas foram: {soma / contador:.2f}C°")