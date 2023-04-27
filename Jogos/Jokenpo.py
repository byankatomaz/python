import random

opcoes = ['Pedra', 'Papel', 'Tesoura']
escolha = " "


def Jokenpo():
    jogada = random.choice(opcoes)
    print(' ')
    print('-=-' * 10)
    print('Vamos iniciar o Jokênpo!')
    print('-=-' * 10)
    print('Já fiz minha jogada! Faça a sua:')
    print('│ Pedra     │')
    print('│ Papel     │')
    print('│ Tesoura   │')
    print('│ Sair      │')
    print("-=-" * 10)

    escolha = input('Digite a sua escolha: ').capitalize().strip()

    if jogada == 'Pedra' and escolha == 'Tesoura':
        pass
        print(f'\nA minha jogada foi: {jogada}')
        print('Eu ganhei!!!')

    elif jogada == 'Papel' and escolha == 'Pedra':
        pass
        print(f'\nA minha jogada foi: {jogada}')
        print('Eu ganhei!!!')

    elif jogada == 'Tesoura' and escolha == 'Papel':
        pass
        print(f'\nA minha jogada foi: {jogada}')
        print('Eu ganhei!!!')

    elif escolha == 'Sair':
        pass
        print('Até logo!')

    elif jogada == escolha:
        pass
        print(f'\nA minha jogada foi: {jogada}')

        while True:
            esco = input(f'Oh não! Fizemos jogadas iguais, vamos de novo? (s/n): ').upper().strip()
            if esco == 'N':
                print('Ah, que pena! Até mais!')
                break
            Jokenpo()
            break

    else:
        pass
        print(f'\nA minha jogada foi: {jogada}')
        print('Ah não! Você ganhou :(')


if __name__ == '__main__':
    Jokenpo()