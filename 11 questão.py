#Faça um programa para escrever os múltiplos de 3 que estão entre 150 e 1000 (inclusive)

numeros = []
cont = 0

for i in range(150, 1000, 2):
    if i % 3 == 0:
        numeros.append(i)
    else:
        cont
print(f'Os números multiplos de 3 {numeros}')
