from gameboard import *

class Battle:

    def __init__(self):

        self.benefits_player = False
        self.benefits_bot = False
        self.nailedIt = False
        self.userInit = False
        self.botInit = False
        self.botWin = False
        self.userWin = False
        self.iWin = False


        self.gameInitTwo()

    def gameInitTwo(self):

        self.game = Game()

        self.game.gameInit()
        self.lista = self.game.data_pokemons
        
        self.user = self.lista[0]
        self.bot = self.lista[1]

        self.benefits()
        self.whoStarts()
    

    def whoStarts(self):
     
        if self.user.speed > self.bot.speed:
            print('You start\n')

            self.userInit = True

            self.attackUser()
        
        elif self.user.speed == self.bot.speed:

            choices = ['I start\n', 'You start\n']
            choice = random.choice(choices)

            print(choice)

            if choice == choices[0]:
                self.botInit = True
                self.attackBot()
                
            else:
                self.userInit = True
                self.attackUser()
        
        else:
            print('I start\n')
            self.botInit = True
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

        print(f'Meu ataque é: {attackUser2}')

        self.damage(attackBot2=None, attackUser2=attackUser2)

        self.gaming()

        
    
    def attackBot(self):

        attacksBot = []

        for attack in self.bot.attack.keys():
            attacksBot.append(attack)
        
        attackBot2 = random.choice(attacksBot)

        print(f'Meu ataque é: {attackBot2}')

        self.damage(attackBot2 = attackBot2, attackUser2=None)

        self.gaming()
    
    

    def nailed(self):


        luck = [False, True]
        weights = [0.6, 0.4]

        self.nailedIt = random.choices(luck, weights)[0]

        if self.nailedIt == True:

            print('Congratulations, you nailed it')
        
        else:

            print('Oh no, you didnt get it right')


    def damage(self, attackBot2 = None, attackUser2 = None):

        self.nailed()

        if self.nailedIt == True:
            
            if self.userInit:
                if self.nailedIt == True and self.benefits_player == True:

                    self.bot.life -= (self.user.attack[attackUser2] * 1.5)

                    print('Bot: ', self.bot.life)
                
                elif self.nailedIt == True and self.benefits_player == False and self.benefits_bot == True:

                    self.bot.life -= (self.user.attack[attackUser2] / 1.5)

                    print('Bot: ', self.bot.life)
                
                else:
                    self.bot.life -= self.user.attack[attackUser2]
                    print('Bot: ', self.bot.life)
            

            elif self.botInit:
                if self.nailedIt == True and self.benefits_bot == True:

                    self.user.life -= (self.bot.attack[attackBot2] * 1.5)

                    print('User: ', self.user.life)
                
                elif self.nailedIt == True and self.benefits_bot == False and self.benefits_player == True:

                    self.user.life -= (self.bot.attack[attackBot2] / 1.5)

                    print('User: ', self.user.life)

                else:

                    self.user.life -= self.bot.attack[attackBot2]
                    print('User: ', self.user.life)


    def gaming(self):

        while True:

            self.win()

            if self.iWin == False:

                if self.userInit == True:

                    while True:
                        self.attackBot()
                        self.attackUser()

                        if self.userWin == True:
                            break
                        elif self.botWin == True:
                            break
                        else:
                            continue
                
                else:

                    while True:
                        self.attackUser()
                        self.attackBot()

                        if self.userWin == True:
                            break
                        elif self.botWin == True:
                            break
                        else:
                            continue
            
            else:
                print('GANHARAM FINALMENTE')
                break
        


    def win(self):

        if self.user.life > 0 and self.bot.life <= 0:
            self.userWin = True
            self.iWin = True
            
        elif self.bot.life > 0 and self.user.life <= 0:
            self.botWin = True
            self.iWin = True

        else:
            pass

Battle()
