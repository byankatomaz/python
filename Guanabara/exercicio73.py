# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.

futebol = ('América - MG', 'Athletico - PR', 'Atlético - MG', 'Bahia',
           'Botafogo', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiabá',
           'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio',
           'Internacional', 'Palmeiras', 'Bragantino', 'Santos',
           'São Paulo', 'Vasco da Gama')

flafla = futebol.index('Flamengo')

print(futebol[:5])
print(futebol[-4:])
print(sorted(futebol))
print(f'O time flamengo está na {flafla} posição.')