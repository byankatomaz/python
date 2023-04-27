# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

def setecinco():
    valores = ()
    nove = 0
    pares = []
    soma = list(valores)

    for i in range(0, 4):
        dado = int(input('Digite um número: '))
        soma.append(dado)
        valores = tuple(soma)

        if dado == 9:
            nove += 1
        elif dado % 2 == 0:
            pares.append(dado)

    print(valores)
    print(f'O numéro 9 apareceu: {nove}')
    print(f'Os números pares colocados foram: {tuple(pares)}')

    if 3 in valores:
        tres = valores.index(3)
        print(f'O número 3 apareceu na posição: {tres}')
    else:
        print('O três não foi digitado')


setecinco()