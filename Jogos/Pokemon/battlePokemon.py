from gameboard import *

class Battle:

    def __init__(self):

        self.benefits_player = False
        self.benefits_bot = False

        self.gameInitTwo()
        self.whoStarts()
        self.benefits()
        self.attackUser()

        print(self.game.typePlayer)
        print(self.game.typeBot)
    
    def gameInitTwo(self):

        self.game = Game()

        self.game.gameInit()
        self.lista = self.game.data_pokemons
        
        self.user = self.lista[0]
        self.bot = self.lista[1]
    

    def whoStarts(self):
     
        if self.user.speed > self.bot.speed:
            print('You start')
        
        elif self.user.speed == self.bot.speed:

            choices = ['I start', 'You start']
            choice = random.choice(choices)

            print(choice)
        
        else:
            print('I start')
    
    def benefits(self):

        if (self.game.typePlayer == "Water" and self.game.typeBot == "Fire"):
            self.benefits_player = True

            print('Player have benefits')

        elif (self.game.typePlayer == "Fire" and self.game.typeBot == "Grass"):
            self.benefits_player = True

            print('Player have benefits')

        elif self.game.typePlayer == "Grass" and self.game.typeBot == "Water":
            self.benefits_player = True

            print('Player have benefits')
        
        elif self.game.typePlayer == self.game.typeBot:
            print('No have benefits for anyone')
        
        else:
            self.benefits_bot = True
            print('Bot have benefits')
    

    def attackUser(self):

        attacks = []

        for attack in self.user.attack.keys():
            print(attack)
            attacks.append(attack)

        questions = [
            inquirer.List('attacks',
                message="Which attack do you want to use?",
                choices=[attacks[0], attacks[1], attacks[2]],
                ),
            ]

        attack = inquirer.prompt(questions)
        


Battle()