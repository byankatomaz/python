from time import sleep
from gameboard import *
import os

class Battle:

    def __init__(self):

        self.benefits_player = False
        self.benefits_bot = False
        self.specialAttack = False
        self.nailedIt = False
        self.turnBot = False
        self.turnUser = False
        self.botWin = False
        self.userWin = False
        self.off = False

        self.gameInitTwo()


    def gameInitTwo(self):

        self.game = Game()

        self.game.gameInit()
        self.lista = self.game.data_pokemons
        
        self.user = self.lista[0]
        self.bot = self.lista[1]

        self.benefits()

        sleep(1)

        self.whoStarts()
    

    def whoStarts(self):
     
        if self.user.speed > self.bot.speed:
            print('You start\n')

            sleep(2)
            self.attackUser()
        
        elif self.user.speed == self.bot.speed:

            choices = ['I start\n', 'You start\n']
            choice = random.choice(choices)

            print(choice)

            if choice == choices[0]:

                sleep(2)
                self.attackBot()
                
            else:

                sleep(2)
                self.attackUser()
        
        else:
            print('I start\n')

            sleep(2)
            self.attackBot()
            
    
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

        self.turnUser = True

        attacks = []

        for attack in self.user.attack.keys():
            attacks.append(attack)

        questions = [
            inquirer.List('attacks2',
                message="Which attack do you want to use?",
                choices=[attacks[0], attacks[1], attacks[2]],
                ),
            ]

        attack_2 = inquirer.prompt(questions)

        attackUser2 = attack_2['attacks2']
        
        print(f'\nCurrent life of your pokemon: {self.user.life:.2f}')
        print(f'Your attack: {attackUser2}')

        self.damage(attackUser2=attackUser2)
        self.gaming()

    
    def attackBot(self):

        self.turnBot = True

        attacksBot = []

        for attack in self.bot.attack.keys():
            attacksBot.append(attack)
        
        attackBot2 = random.choice(attacksBot)

        print(f'\nCurrent life of my pokemon: {self.bot.life:.2f}')
        print(f'My attack: {attackBot2}')

        self.damage(attackBot2 = attackBot2)
        self.gaming()
    

    def nailed(self):


        luck = [False, True]
        weights = [0.4, 0.6]

        self.nailedIt = random.choices(luck, weights)[0]

        if self.nailedIt == True:

            print('Congratulations, you nailed it\n')
        
        else:

            print('Oh no, you didnt get it right\n')


    def damage(self, attackBot2 = None, attackUser2 = None):

        self.nailed()

        if self.nailedIt == True:
            
            if self.turnUser == True:
                if self.benefits_player == True:

                    self.bot.life -= (self.user.attack[attackUser2] * 1.5)
                    print(f'Life of pokemon bot \033[1m{self.bot.name}\033[m: {self.bot.life:.2f}\n')
                
                elif self.benefits_player == False and self.benefits_bot == True:

                    self.bot.life -= (self.user.attack[attackUser2] / 1.5)
                    print(f'Life of pokemon bot \033[1m{self.bot.name}\033[m: {self.bot.life:.2f}\n')
                
                else:
                    self.bot.life -= self.user.attack[attackUser2]
                    print(f'Life of pokemon bot \033[1m{self.bot.name}\033[m: {self.bot.life:.2f}\n')
            

            elif self.turnBot == True:
                if self.benefits_bot == True:

                    self.user.life -= (self.bot.attack[attackBot2] * 1.5)
                    print(f'Life of pokemon user \033[1m{self.user.name}\033[m: {self.user.life:.2f}\n')
                
                elif self.benefits_bot == False and self.benefits_player == True:

                    self.user.life -= (self.bot.attack[attackBot2] / 1.5)
                    print(f'Life of pokemon user \033[1m{self.user.name}\033[m: {self.user.life:.2f}\n')

                else:

                    self.user.life -= self.bot.attack[attackBot2]
                    print(f'Life of pokemon user \033[1m{self.user.name}\033[m: {self.user.life:.2f}\n')


    
    def turns(self):

        while(self.off != True):



            if self.turnUser == True:
                self.turnUser = False
                self.attackBot()
            
            else:
                self.turnBot = False
                self.attackUser()

    def gaming(self):

        while True:

            self.win()

            if self.off:
                break

            sleep(6)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.turns()
            sleep(6)
            os.system('cls' if os.name == 'nt' else 'clear')
    

    def win(self):

        if self.user.life > 0 and self.bot.life <= 0:
            self.userWin = True
            self.off = True

            print('THE USER WINS')

            
        elif self.bot.life > 0 and self.user.life <= 0:
            self.botWin = True
            self.off = True

            print('THE COMPUTER WINS')

        else:
            pass

Battle()
