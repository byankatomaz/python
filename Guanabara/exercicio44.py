#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal

#– 3x ou mais no cartão: 20% de juros

import time


def pensando():
    print('Certo! Calculando a sua compra...\n')

    time.sleep(3)


def pagamento():

    print('Vamos confirmar quanto deu as suas compras: ')
    valor = float(input('Digite o valor da sua compra: '))

    print(f'-=-'*13)
    print('* Escolha a forma de pagamento *')
    print(f'-=-'*13)
    print('│ [1] Á vista/Dinheiro                │')
    print('│ [2] Á vista no cartão               │')
    print('│ [3] 2x no cartão de crédito         │')
    print('│ [4] 3x ou mais no cartão de crédito │')
    print('│ [5] Sair                            │')
    print(f'-=-'*13)

    option = int(input('Digite o número da opção:  '))
    print(f'-=-' * 13)

    match option:
        case 1:

            pensando()

            valordesconto = valor*0.10
            valornovo = valor - valordesconto
            print(f'O valor a ser pago será: R${valornovo:.2f}')

        case 2:

            pensando()

            valordescont = valor * 0.05
            valornov = valor - valordescont
            print(f'O valor a ser pago será: R${valornov:.2f}')

        case 3:

            pensando()

            valorparc = valor/2
            print(f'O valor a ser pago será: R${valor:.2f}')
            print(f'Com o total de parcelas, ele ficará: R${valorparc:.2f} por mês')

        case 4:

            pensando()

            parcelas = int(input('Digite o valor das parcelas: '))
            juros = valor*0.20
            valorcomjuros = valor + juros
            valorparce = valorcomjuros / parcelas

            print(f'\nO valor a ser pago com juros será: R${valorcomjuros:.2f}')
            print(f'Com o total de parcelas, ele ficará: R${valorparce:.2f} por mês')

        case 5:
            print('Okay! Até a próxima!')

        case _:
            print('O número que digitou não está nas opções.')


if __name__ == '__main__':
    pagamento()