#Altere o programa anterior (questão 3) para mostrar no final a soma dos números.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
numeros = []

while num2<num1:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
else:
    for i in range(num1 +1, num2, 1):
        numeros.append(i)
    soma_numeros = sum(numeros) 
    print(f"Os números entre os números digitados são: {numeros}")
    print(f"A soma dos valores entre os números digitados é de: {soma_numeros}")
    