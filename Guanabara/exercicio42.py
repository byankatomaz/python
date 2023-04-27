#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

print('Vamos confirmar qual tipo de triângulo esses números podem formar: \n')
lado1 = float(input('Digite o primeiro número: '))
lado2 = float(input('Digite o segundo número: '))
lado3 = float(input('Digite o terceiro número: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('\nOs números podem formar um triângulo!')

    if lado1 == lado2 == lado3:
        print('E é um triângulo Equilátero')

    elif lado1 != lado2 != lado3 != lado1:
        print('E é um triângulo Escaleno!')

    else:
        print('E é um triângulo Isóceles')

else:
    print('Os números não podem formar um triângulo')