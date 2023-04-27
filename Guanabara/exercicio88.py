# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from time import sleep
import random


def mega_sena():

    lista_sorteado = []
    copia = []

    print('-=-'*10)
    print('Jogo da Mega Sena'.center(30))
    print('-=-'*10)
    print()
    jogos = int(input('Digite quantos jogos deseja fazer: '))
    print()
    print('-=-'*3, end='')
    print(f'Sorteando {jogos} jogos', end='')
    print('-=-'*3)
    print()
    sleep(1)
    total = 1

    while total <= jogos:
        cont = 0

        while True:
            sorteado = random.randint(1, 60)

            if sorteado not in copia:
                copia.append(sorteado)
                cont += 1

            if cont >= 6:
                break

        copia.sort()
        lista_sorteado.append(copia[:])
        copia.clear()
        total += 1

    for i, l in enumerate(lista_sorteado):
        print(f'Jogo {i+1}: {l}')
    print()
    print('-=-' * 4, end='')
    print(f'BOA SORTE', end='')
    print('-=-' * 4)
    print()
mega_sena()