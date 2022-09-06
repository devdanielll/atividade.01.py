#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares

numero = 1
impar = 0
par = 0

while numero <= 10:
    a = int(input("Digite um número: "))
    numero = numero + 1
    if a % 2 == 0:
        a = par
        par = par + 1
    else:
        a = impar
        impar = impar + 1
print("A quantidade de números impares é: ", impar)
print("A quantidade de números pares é: ", par)
