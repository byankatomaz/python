# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

def unico():

    numeros = []
    pares = []
    impares = []

    for n in range(7):
        num = int(input(f'Digite o numero {n+1}º número: '))

        if num % 2 == 0:
            pares.append(num)

        if num % 2 != 0:
            impares.append(num)

    numeros.append(pares[:])
    numeros.append(impares[:])

    print(f'\nOs valores pares digitados foram: ', sorted(numeros[0]))
    print(f'Os valores impares digitados foram: ', sorted(numeros[1]))


unico()