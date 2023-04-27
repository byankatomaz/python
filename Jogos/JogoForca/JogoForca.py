import sys

from timee import start_thread, cancel_thread, start_thread2, cancel_thread2, Termino
from xml.dom import minidom
import random
import time
import requests
import inquirer


class Jogo:

    def __init__(self):

        self.palavraselecionada = None
        self.termino = None
        self.dicadapalavra = None
        self.chute = None
        self.tempoini = None
        self.dicasPalavra = []
        self.palavrasecreta = None
        self.palavras = []
        self.tamletra = []
        self.vidas = 6
        self.tamanho = 0
        self.letrasErradas = []
        self.letrasCorretas = []
        self.adicionais = []
        self.dicasadicionais = []
        self.listadaspalavras = []

    # ----------------------------------------------------------------------------------------------------------------------

    def Inicio(self):
        print('-=-' * 20)
        print('O jogo da Forca!'.center(60, ' '))
        print('-=-' * 20)

        time.sleep(1)

        questions = [
            inquirer.List('comando',
                          message='Deseja iniciar?',
                          choices=['SIM', 'NÃO'],
                          ),
        ]
        answers = inquirer.prompt(questions)

        print('-=-' * 20)

        if answers['comando'] == 'SIM':
            print('VAMOS INICIAR!!'.center(60, ' '))
            print('-=-' * 20)
            time.sleep(1)
            self.Escolha()

        elif answers['comando'] == 'NÃO':
            print('Okay! Até a proxima!'.center(90, ' '))
            print('-=-' * 30)

    # ----------------------------------------------------------------------------------------------------------------------

    def Escolha(self):

        questions = [
            inquirer.List('escolha',
                          message='Escolha a sua modalidade',
                          choices=['Nutella', 'Café com leite', 'Hard Raiz', 'Sair'],
                          ),
        ]
        escolhausu = inquirer.prompt(questions)

        print()
        print("-=-" * 5)

        if escolhausu['escolha'] == 'Nutella':
            self.Nutella()

        elif escolhausu['escolha'] == 'Café com leite':
            self.Cafe()

        elif escolhausu['escolha'] == 'Hard Raiz':
            self.Hard()

        else:
            print('Okaay! Até outro momento!')

    # ----------------------------------------------------------------------------------------------------------------------

    def Nutella(self):

        self.Definindo()

        while True:

            print(' ')
            print("-=-" * 10)
            print(' ')
            self.chute = input('Digite uma letra: ').upper().strip()

            if self.chute == self.palavrasecreta:

                print(' ')
                print("-=-" * 10)
                self.Boneco()
                print(f'Dica: {self.dicadapalavra}')
                print(' ')
                self.ChuteUsu()

                if self.Ganhou() is True:
                    print(' ')
                    print("-=-" * 10)
                    print('\nVOCÊ ACERTOU A PALAVRA! PARABÈNS')
                    self.JogandoNovamente()
                    break

            if self.chute in self.letrasCorretas or self.chute in self.letrasErradas:

                print(' ')
                print("-=-" * 10)
                self.Boneco()
                print(f'Dica: {self.dicadapalavra}')
                print(' ')
                print('Você já chutou essa letra, tente outra.')

                self.ChuteUsu()

            elif self.chute in self.palavrasecreta:
                print(' ')
                print("-=-" * 10)
                self.Boneco()
                print(f'Dica: {self.dicadapalavra}')
                print(' ')
                print('Parabéns! A letra está na palavra!')
                self.letrasCorretas.append(self.chute)

                self.ChuteUsu()

                if self.Ganhou() is True:
                    print(' ')
                    print("-=-" * 10)
                    print('\nVOCÊ ACERTOU A PALAVRA! PARABÈNS')
                    self.JogandoNovamente()
                    break

            elif self.chute not in self.palavrasecreta:

                self.letrasErradas.append(self.chute)
                self.vidas -= 1
                print(' ')
                print("-=-" * 10)
                self.Boneco()
                print(f'Dica: {self.dicadapalavra}')
                print(' ')
                print('Ah, que pena, a letra não está na palavra')

                self.ChuteUsu()

                if self.Perdeu() is True:
                    self.JogandoNovamente()
                    break

    # ----------------------------------------------------------------------------------------------------------------------

    def Cafe(self):

        self.Adicionando()
        print('\nVocê terá 30 segundos para acertar a palavra!!')
        self.Definindo()
        self.tempoini = start_thread()

        while True:

            print(' ')
            print("-=-" * 10)
            print(' ')
            self.chute = input('Digite uma letra: ').upper().strip()

            if self.chute == self.palavrasecreta:

                print(' ')
                print("-=-" * 10)
                self.Boneco()
                print(f'Dica: {self.dicadapalavra}')
                print(' ')
                self.ChuteUsu()

                if self.Ganhou() is True:
                    print(' ')
                    print("-=-" * 10)
                    print('\nVOCÊ ACERTOU A PALAVRA! PARABÈNS')
                    cancel_thread(self.tempoini)
                    self.JogandoNovamente()
                    break

            if self.chute in self.letrasCorretas or self.chute in self.letrasErradas:

                print(' ')
                print("-=-" * 10)
                self.Boneco()
                print(f'Dica: {self.dicadapalavra}')
                print(' ')
                print('Você já chutou essa letra, tente outra.')

                self.ChuteUsu()

            elif self.chute in self.palavrasecreta:
                print(' ')
                print("-=-" * 10)
                self.Boneco()
                print(f'Dica: {self.dicadapalavra}')
                print(' ')
                print('Parabéns! A letra está na palavra!')
                self.letrasCorretas.append(self.chute)

                self.ChuteUsu()

                if self.Ganhou() is True:
                    print(' ')
                    print("-=-" * 10)
                    print('\nVOCÊ ACERTOU A PALAVRA! PARABÈNS')
                    cancel_thread(self.tempoini)
                    self.JogandoNovamente()
                    break

            elif self.chute not in self.palavrasecreta:

                self.letrasErradas.append(self.chute)
                self.vidas -= 1
                print(' ')
                print("-=-" * 10)
                self.Boneco()
                print(f'Dica: {self.dicadapalavra}')
                print(' ')
                print('Ah, que pena, a letra não está na palavra')

                self.ChuteUsu()

                if self.Perdeu() is True:
                    cancel_thread(self.tempoini)
                    self.JogandoNovamente()
                    break

    # ----------------------------------------------------------------------------------------------------------------------

    def Hard(self):

        print('\nVocê terá 20 segundos para acertar a palavra!!')
        self.Definindo2()
        self.tempoini = start_thread2()

        while True:

            print(' ')
            print("-=-" * 10)
            print(' ')
            self.chute = input('Digite uma letra: ').strip().lower()

            if self.chute == self.palavrasecreta:

                print(' ')
                print("-=-" * 10)
                self.Boneco()
                print(f'Dica: {self.dicadapalavra}')
                print(' ')
                self.ChuteUsu()

                if self.Ganhou() is True:
                    print(' ')
                    print("-=-" * 10)
                    print('\nVOCÊ ACERTOU A PALAVRA! PARABÈNS')
                    cancel_thread2(self.tempoini)
                    self.JogandoNovamente()
                    break

            if self.chute in self.letrasCorretas or self.chute in self.letrasErradas:

                print(' ')
                print("-=-" * 10)
                self.Boneco()
                print(f'Dica: {self.dicadapalavra}')
                print(' ')
                print('Você já chutou essa letra, tente outra.')

                self.ChuteUsu()

            elif self.chute in self.palavrasecreta:
                print(' ')
                print("-=-" * 10)
                self.Boneco()
                print(f'Dica: {self.dicadapalavra}')
                print(' ')
                print('Parabéns! A letra está na palavra!')
                self.letrasCorretas.append(self.chute)

                self.ChuteUsu()

                if self.Ganhou() is True:
                    print(' ')
                    print("-=-" * 10)
                    print('\nVOCÊ ACERTOU A PALAVRA! PARABÈNS')
                    cancel_thread2(self.tempoini)
                    self.JogandoNovamente()
                    break

            elif self.chute not in self.palavrasecreta:

                self.letrasErradas.append(self.chute)
                self.vidas -= 1
                print(' ')
                print("-=-" * 10)
                self.Boneco()
                print(f'Dica: {self.dicadapalavra}')
                print(' ')
                print('Ah, que pena, a letra não está na palavra')

                self.ChuteUsu()

                if self.Perdeu() is True:
                    cancel_thread2(self.tempoini)
                    self.JogandoNovamente()
                    break

    # ----------------------------------------------------------------------------------------------------------------------

    def Ganhou(self):

        if self.chute == self.palavrasecreta:
            return True
        else:
            for self.chute in self.palavrasecreta:
                if self.chute not in self.letrasCorretas:
                    return False
            return True

    # ----------------------------------------------------------------------------------------------------------------------

    def Perdeu(self):

        if self.vidas == 0:
            print(' ')
            print("-=-" * 10)
            print(f'\nSuas vidas acabaram, a palavra secreta era {self.palavrasecreta}')
            print(' ')
            print("-=-" * 10)
            return True
        return False

    # ----------------------------------------------------------------------------------------------------------------------

    def ChuteUsu(self):

        if self.chute == self.palavrasecreta:
            print(self.palavrasecreta)
        else:
            for self.chute in self.palavrasecreta:
                if self.chute in self.letrasCorretas:
                    print(self.chute, end=" ")
                else:
                    print("_", end=" ")

    # ----------------------------------------------------------------------------------------------------------------------

    def Definindo(self):

        self.Secreto()
        self.Boneco()
        posicao = self.palavras.index(self.palavrasecreta)
        self.dicadapalavra = self.dicasPalavra[posicao]
        print(f'Dica: {self.dicadapalavra}')
        self.tamanho = len(self.palavrasecreta)

        for i in range(self.tamanho):
            self.tamletra.append('_')
        print(' '.join(self.tamletra))

    # ----------------------------------------------------------------------------------------------------------------------

    def Definindo2(self):

        self.Secreto2()
        self.Boneco()
        print(f'Dica: {self.dicadapalavra}')
        self.tamanho = len(self.palavrasecreta)

        for i in range(self.tamanho):
            self.tamletra.append('_')
        print(' '.join(self.tamletra))

    # ----------------------------------------------------------------------------------------------------------------------

    def Adicionando(self):

        while True:

            print(' ')
            decisao = input('Você deseja adicionar uma palavra? (S/N): ').upper()

            if decisao in 'SIMS':
                print(' ')
                print("-=-" * 10)
                palavradicional = input('Adicione uma palavra: ').upper()
                self.adicionais.append(palavradicional)
                self.palavras.extend(self.adicionais)
                print("-=-" * 10)
                dicadicional = input('Agora digite a dica para essa palavra: ')
                self.dicasPalavra.append(dicadicional)
                print("-=-" * 10)

            elif decisao in 'NÃONAON':
                print(' ')
                print("-=-" * 10)
                break

    # ----------------------------------------------------------------------------------------------------------------------

    def JogandoNovamente(self):

        while True:

            print(' ')
            decisao = input('Você quer jogar outra partida? (S/N): ').upper()

            if decisao in 'SIMS':

                self.vidas = 6
                self.letrasErradas[:] = []
                self.letrasCorretas[:] = []
                self.tamletra[:] = []
                self.Escolha()

            elif decisao in 'NÃONAON':
                print(' ')
                print('-=-' * 10)
                print('\nOkay! até a próxima!')
                sys.exit()

    # ----------------------------------------------------------------------------------------------------------------------

    def Secreto(self):

        self.palavras = ["ALBATROZ", "ALPACA", "ANCHOVA", "BACALHAU", "BADEJO", "BARRACUDA", "BELUGA", "CAGADO",
                         "CHINCHILA", "CRACA", "DROMEDARIO", "ESCARAVELHO", "GERBO",
                         "GNU", "GRALHA", "HAMSTER", "LEMURE", "LHAMA", "LINCE", "MARRECO", "MELRO", "OCAPI", "OURICO",
                         "PELICANO", "PERCEVEJO", "PIRILAMPO", "QUATI", "ROUXINOL", "SANGUESSUGA",
                         "SURUCUCU", "TAPIR", "TEXUGO", "VISON", "ZEBU"]

        self.dicasPalavra = ["Ave marinha com asas enormes", "Animal da família dos camelos",
                             "Peixe de água salgada muito saboroso",
                             "Um dos peixes mais consumidos no mundo",
                             "Peixe de água salgada, também conhecido como robalo",
                             "Peixe com dentes afiados e corpo esguio", "Espécie de baleia branca",
                             "Réptil que vive em ambientes aquáticos",
                             "Animal peludo e fofo, muito utilizado para a produção de roupas",
                             "Crustáceo que vive em superfícies duras, como rochas e cascos de navios ",
                             "Animal da família dos camelos com apenas uma corcova",
                             "Inseto que é conhecido por sua beleza e brilho",
                             "Roedor de pequeno porte com cauda longa",
                             "Espécie de antílope com barba longa", "Ave com plumagem negra e bico curvo",
                             "Roedor muito popular como animal de estimação", "Animal que vive na ilha de Madagascar",
                             "Animal doméstico da família dos camelos", "Felino de médio porte com orelhas pontudas",
                             "Ave aquática muito saborosa", "Pássaro preto com bico amarelo",
                             "Animal que se parece com uma zebra, mas sem as listras nas patas",
                             "Animal coberto de espinhos", "Ave aquática com uma bolsa na garganta",
                             "Inseto pequeno e chato, que se alimenta do sangue de animais e humanos",
                             "Inseto luminoso que emite luz na escuridão", "Animal comum em regiões de mata atlântica",
                             "Ave que tem um canto melodioso e agradável de ouvir.",
                             "Animal que se alimenta de sangue de outros animais e pode transmitir doenças.",
                             "Cobra venenosa encontrada na América do Sul.",
                             "Animal com aparência de porco, encontrado em regiões da América do Sul e Central.",
                             "Animal com pelagem densa e preênsil, encontrado em diversos locais do mundo.",
                             "Animal carnívoro com pelagem densa e macia, encontrado em diversas regiões do mundo.",
                             "Animal bovino originário da Índia, utilizado para tração e produção de leite."]

        while True:

            self.palavraselecionada = random.choice(self.palavras)
            self.listadaspalavras.append(self.palavraselecionada)

            if self.palavraselecionada \
                    in self.listadaspalavras:
                self.palavrasecreta = self.palavraselecionada
            break

        return self.palavras, self.dicasPalavra

    # ----------------------------------------------------------------------------------------------------------------------

    def Secreto2(self):

        url1 = "https://api.dicionario-aberto.net/random"
        palavras2 = requests.get(url1)
        palavras2 = palavras2.json()["word"]
        self.palavrasecreta = palavras2

        dica = requests.get(f"https://api.dicionario-aberto.net/word/{palavras2}")
        url = dica.json()[0]["xml"]
        parserxml = minidom.parseString(url)
        tag = parserxml.getElementsByTagName("def")

        for i in tag:
            self.dicadapalavra = i.firstChild.nodeValue
        return palavras2

    # ----------------------------------------------------------------------------------------------------------------------

    def Boneco(self):

        boneco_forca = [
            '  +---+',
            '  |   |',
            '      |',
            '      |',
            '      |',
            '      |',
            '========='
        ]

        if self.vidas <= 5:
            boneco_forca[2] = '  O   |'
        if self.vidas <= 4:
            boneco_forca[3] = ' /    |'
        if self.vidas <= 3:
            boneco_forca[3] = ' / \  |'
        if self.vidas <= 2:
            boneco_forca[3] = ' /|\  |'
        if self.vidas <= 1:
            boneco_forca[4] = ' /    |'
        if self.vidas < 1:
            boneco_forca[4] = ' / \  |'

        for linha in boneco_forca:
            print(linha)


if __name__ == '__main__':
    chama = Jogo()
    chama.Inicio()

# ----------------------------------------------------------------------------------------------------------------------
