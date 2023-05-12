class Pokemon():
    def __init__(self, name, attack, defense, speed):
        self.type = ''
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed


class Water(Pokemon):
    type = 'Water'
    def __init__(self, life, name, attack, defense, speed):
        super().__init__(name, attack, defense, speed)
        self.life = life
        #self.speAttack = speAttack
        #self.speDefense = speDefense


    def WaterPokes(self):

        self.pokemons = [
            {"name": "Kyogre", "life": 770, "attack" : {'Blizzard': 100, 'Thunder': 110, 'To surf': 100}, 'defense': 90, 'speAttack': {'Water jet': 150, 'Waterfall': 140}, 'speDefense': 160, 'speed': 90},
            {"name": "Palkia", "life": 680, "attack" : {'Fire Blast': 140, 'Hydro pump': 130, 'Aqua Tail': 50}, 'defense': 100, 'speAttack': {'Draco Meteor': 150, 'Spacial Rend': 135}, 'speDefense': 120, 'speed': 120},
            {"name": "Blastoise", "life": 630, "attack" : {'Water Gun': 122, 'Rapid Spin': 110, 'To surf': 100}, 'defense': 120, 'speAttack': {'Ice Beam': 150, 'Hydro Cannon': 140}, 'speDefense': 115, 'speed': 90}
        ]

        return self.pokemons


class Grass(Pokemon):
    type = 'Grass'
    def __init__(self, name, life, attack, defense, speAttack, speDefense, speed):
        super().__init__(name, defense, speed)
        self.life = life
        self.speAttack = speAttack
        self.speDefense = speDefense


    def GrassPokes(self):

        self.pokemons = [
            {"name": "Zarude", "life": 650, "attack" : {'Multiple Whiplash': 115, 'Suction Vines': 100, 'Jungle Rage': 119}, 'defense': 105, 'speAttack': {'Leaf Guard': 150, 'Jungle Explosion': 145}, 'speDefense': 120, 'speed': 105},
            {"name": "Venusaur", "life": 780, "attack" : {'Jungle Totem': 140, 'Dangerous Pollen': 130, 'Wobbly Loop': 100}, 'defense': 100, 'speAttack': {'Overgrow': 150, 'Sunshine': 130}, 'speDefense': 160, 'speed': 100},
            {"name": "Roserade", "life": 630, "attack" : {'Sweet Scent': 125, 'Poison Sting': 120, 'Petal Dance': 105}, 'defense': 120, 'speAttack': {'Energy Ball': 150, 'Solar Beam': 140}, 'speDefense': 125, 'speed': 90}
        ]

        life = self.pokemons['life']

        return self.pokemons, life
    

class Fire(Pokemon):
    type = 'Fire'
    def __init__(self, life, speAttack, speDefense, name, type, attack, defense, speed):
        super().__init__(name, type, attack, defense, speed)
        self.life = life
        self.speAttack = speAttack
        self.speDefense = speDefense

    def FirePokes(self):

        self.pokemons = [
            {"name": "Reshiram", "life": 680, "attack" : {'Flamethrower': 100, 'Fusion Flare': 110, 'Dragon Claw': 100}, 'defense': 100, 'speAttack': {'Turboblaze': 150, 'Blue Fire': 130}, 'speDefense': 120, 'speed': 90},
            {"name": "Charizard", "life": 750, "attack" : {'Slash': 140, 'Dragon breath': 130, 'Blaze': 90}, 'defense': 100, 'speAttack': {'Solar Power': 150, 'Hurricane Flame': 140}, 'speDefense': 160, 'speed': 120},
            {"name": "Volcarona", "life": 650, "attack" : {'Heat Wave': 122, 'Bug Buzz': 100, 'Fiery Dance': 80}, 'defense': 65, 'speAttack': {'Flame Body': 150, 'Flare Blitz': 150}, 'speDefense': 105, 'speed': 100}
        ]

        return self.pokemons
    
    
    
    
    
    
    
    
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    from pokemon import Water, Grass, Fire
import inquirer

class Game:
    def __init__(self, time = 90):
        self.typePlayer = ''
        self.time = time


    def optionUser(self):

        questions = [
            inquirer.List('elements',
                message="Which element do you want to choose?",
                choices=[Water.type, Grass.type, Fire.type],
                ),
            ]
        
        elements = inquirer.prompt(questions)
        self.typePlayer = elements
        
        if elements['elements'] == 'Grass':
            
            questions = [
            inquirer.List('pokemons',
                message="Which pokemon do you want to choose?",
                choices=['Zarude', 'Venusaur', 'Roserade'],
                ),
            ]
        
        pokemons = inquirer.prompt(questions)
        print(pokemons)

        if elements['pokemons'] == 'Zarude':
            poke = Grass()

        

game = Game()
game.optionUser()
