# Complemente o exercicio anterior (8 questão) mostrando todos os divisores dos numeros

num = int(input ("Digite um número: "))
cont = 0
div = []

for i in range(num):
    if num % ( i + 1 ) == 0:
        cont += 1
        div.append( i + 1 )
    else:
        cont

if cont == 2:
    print ("O numero é primo divisivel por ",div)
else:
    print ("O numero não é primo pois é divisivel por ",div)