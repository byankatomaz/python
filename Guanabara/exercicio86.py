# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.


def matriz():

    tab = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    for l in range(3):
        for c in range(3):

            tab[l][c] = int(input(f'Digite o valor de {l}{c}: '))
    print('-=-'*30)

    for l in range(3):
        for c in range(3):
            print(f'[{tab[l][c]:^5}]', end=' ')
        print()


matriz()