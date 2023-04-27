# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

def comparando():

    dados = []
    pessoa = []
    total = 0
    maior = menor = 0

    while True:

        decisao = input('\nVocê deseja cadastrar uma pessoa? (S/N): '). upper()

        if decisao == "S":

            total += 1
            nome = input('Digite o nome da pessoa: ')
            pessoa.append(nome)
            peso = int(input('Digite seu peso: '))
            pessoa.append(peso)

            if len(dados) == 0:
                maior = menor = pessoa[1]
            else:
                if pessoa[1] > maior:
                    maior = pessoa[1]
                if pessoa[1] < menor:
                    menor = pessoa[1]

            dados.append(pessoa[:])
            pessoa.clear()

        elif decisao == "N":

            print(' ')
            print('-=-'*10)
            print(f'\nVocê cadastrou {total} pessoas.')

            for peso in dados:
                if peso[1] == maior:
                    print(f'{peso[0]} teve o maior peso, que é de {maior}')
                if peso[1] == menor:
                    print(f'{peso[0]} teve o menor peso, que é de {menor}')
            break


comparando()