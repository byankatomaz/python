#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
import time
import os


def termino2():
    pid = os.getpid()
    os.kill(pid, 0)


def inicio():

    print('-=-' * 30)
    print('                                   O jogo do Par ou Impar!')
    print('-=-' * 30)

    time.sleep(1)

    comando = input('                           Deseja iniciar? (Sim/Não): ').upper().strip()

    if comando == 'SIM' or comando in 'S':
        print('                                    VAMOS INICIAR!!')
        print('-=-' * 30)
        print('                             Ja fiz minha jogada faça a sua!')
        time.sleep(1)
    elif comando in 'NÃONAO' or comando in 'N':
        print('                                 Okay! Até a proxima!')
        print('-=-' * 30)
        termino2()
    else:
        print('                          O comando dado não está nas opções.')
        inicio()

    def comando():
        cont = 0

        while True:
            secreto = random.randint(0, 101)
            jogada = int(input('Digite um número de 0 a 100: '))
            escolha = input('Você quer par ou impar? (P/I): ').strip().upper()
            print('-=-' * 30)

            if escolha in 'PARP':
                divi = (jogada + secreto) % 2
                if divi == 0:
                    print(f'\n                           ***** Eu joguei o número: {secreto} *****')
                    print('                        ***** Você ganhou! Vamos novamente *****\n')
                    print('-=-' * 30)
                    cont += 1
                    continue
                print(f'                             ***** Eu joguei o número: {secreto} *****')
                print(f'                         ***** Eu ganhei! Suas vitórias foram: {cont} *****')
                print('                                        **Até mais**')
                print('-=-' * 30)
                termino2()

            elif escolha in 'IMPARI':
                divi = (jogada + secreto) % 2
                if divi != 0:
                    print(f'\n                           ***** Eu joguei o número: {secreto} *****')
                    print('                        ***** Você ganhou! Vamos novamente *****\n')
                    print('-=-' * 30)
                    cont += 1
                    continue
                print(f'                             ***** Eu joguei o número: {secreto} *****')
                print(f'                         ***** Eu ganhei! Suas vitórias foram: {cont} *****')
                print('                                        **Até mais**')
                print('-=-' * 30)
                termino2()
            else:
                print('                          O comando dado não está nas opções.')
                print('-=-' * 30)
                comando()

    comando()


if __name__ == '__main__':

    inicio()
