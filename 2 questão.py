#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

impares = []
for i in range(1,50,2):
    impares.append(i)
print(f'Os números impares entre 1 e 50 são: {impares}')