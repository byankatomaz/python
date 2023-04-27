#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Vamos confirmar se os três números digitados podem formar um triângulo: \n')
lado1 = float(input('Digite o primeiro número: '))
lado2 = float(input('Digite o segundo número: '))
lado3 = float(input('Digite o terceiro número: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os números podem formar um triângulo!')
else:
    print('Os números não podem formar um triângulo')