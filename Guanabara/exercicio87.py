# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

def matriz():

    pares = 0
    somalinha = 0

    tab = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    for l in range(3):
        for c in range(3):
            num = int(input(f'Digite o valor de {l}{c}: '))
            tab[l][c] = num

            if c == 2:
                somalinha += num

            if num % 2 == 0:
                pares += num

    print('-=-'*30)
    for l in range(3):
        for c in range(3):
            print(f'[{tab[l][c]:^5}]', end=' ')
        print()

    print(f'\nA soma dos numeros pares digitados é: {pares}')
    print(f'A soma dos valores da terceira coluna é: {somalinha}')
    print(f'E o maior número da segunda coluna é: {max(tab[1])}')


matriz()