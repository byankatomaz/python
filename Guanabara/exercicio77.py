# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Jurema', 'Fernanada', 'Gabrielly', 'Beatriz', 'Maria', 'Bianca', 'Victor', 'Carol')
palavra = ' '
for p in range(len(palavras)):
    palavra = palavras[p]
    print(f'\nDentro da palavra {palavra} temos as vogais: ', end='')
    for letras in palavra:
        if letras in 'aeiou':
            print(letras, end=' ')