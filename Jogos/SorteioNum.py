import random
import os
import time
from threading import Timer


def termino2():
    print('Acabou o seu tempo!!')
    pid = os.getpid()
    os.kill(pid, -1)


def termino():
    pid = os.getpid()
    os.kill(pid, -1)


def tempo():
    tempoini = Timer(30, termino2)
    tempoini.start()


def sorteio():

    sorteado = int(random.randrange(0, 101))
    print('-' * 30)
    print('Vamos iniciar o jogo de sorteio!')
    print('-' * 30)

    time.sleep(1)

    vida = 50
    tentativas = 3
    tempo = 30
    print('-' * 30)
    print(f'Você terá apenas: {vida} vidas')
    print(f'Você terá apenas: {tentativas} tentativas')
    print(f'Você terá apenas: {tempo} segundos para terminar')
    print('-' * 30)
    time.sleep(0.5)

    while tentativas <= 3:
        num_user = int(input("\nInsira seu chute!: "))
        if num_user != sorteado:
            diferenca = abs(num_user - sorteado)
            vida -= diferenca
            print(f'Errou! O número sorteado não foi esse!')
            print(f'Agora você tem: {tentativas - 1} tentativas')
            print(f'E ainda possui: {vida} vidas\n')
            print('-' * 30)
            pass

            if vida <= 0:
                print('\nSuas vidas acabaram')
                print('Você perdeu')
                print(f'\nO numero sorteado foi: {sorteado}')

                termino()

        else:
            print(f'\nParabéns! Você acertou o número!')
            print('Você ganhou!')
            print('-' * 30)
            break

        tentativas = tentativas - 1

        if tentativas == 0:
            print('\nVocê perdeu!!')
            print(f'O numero sorteado foi: {sorteado}')
            print('-' * 30)
            break

    termino()


if __name__ == '__main__':
    tempo()
    sorteio()