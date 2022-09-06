#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

while num2<num1:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
else:
    for i in range(num1 +1, num2, 1):
        print(i)
    