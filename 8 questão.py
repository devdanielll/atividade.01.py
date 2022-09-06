# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input ("Digite um número: "))
cont = 0

for i in range(num):
    if num % ( i + 1 ) == 0:
        cont += 1
    else:
        cont
        
if cont == 2:
    print (f"O numero {num} é primo")
else:
    print (f"O numero {num} não é primo")