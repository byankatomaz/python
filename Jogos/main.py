class Pokemon:
    def __init__(self, name, attack, defense, speed):
        self.type = ''
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed

class Water(Pokemon):
    type = 'Water'
    def __init__(self, life, speAttack, speDefense, name, attack, defense, speed):
        super().__init__(name, attack, defense, speed)
        self.life = life
        self.speAttack = speAttack
        self.speDefense = speDefense


    def WaterPokes(self):

        self.pokemons = [
            {"name": "Kyogre", "life": 100, "attack" : {'Blizzard': 100, 'Thunder': 110, 'To surf': 100}, 'defense': 90, 'speAttack': {'Water jet': 150, 'Waterfall': 150}, 'speDefense': 160, 'speed': 90},
            {"name": "Kyogre", "life": 100, "attack" : {'Blizzard': 100, 'Thunder': 110, 'To surf': 100}, 'defense': 90, 'speAttack': {'Water jet': 150, 'Waterfall': 150}, 'speDefense': 160, 'speed': 90},
            {"name": "Kyogre", "life": 100, "attack" : {'Blizzard': 100, 'Thunder': 110, 'To surf': 100}, 'defense': 90, 'speAttack': {'Water jet': 150, 'Waterfall': 150}, 'speDefense': 160, 'speed': 90}
        ]

        name = 'Kyogre'
        life = 100
        attack = 150
        defense = 90
        speAttack = 180
        speDefense = 160
        speed = 90

        return name, life, attack, defense, speAttack, speDefense, speed




class Grass(Pokemon):
    def __init__(self, life, speAttack, speDefense, name, type, attack, defense, speed):
        super().__init__(name, type, attack, defense, speed)
        self.type = 'Grass'
        self.life = life
        self.speAttack = speAttack
        self.speDefense = speDefense

class Fire(Pokemon):
    def __init__(self, life, speAttack, speDefense, name, type, attack, defense, speed):
        super().__init__(name, type, attack, defense, speed)
        self.type = 'Fire'
        self.life = life
        self.speAttack = speAttack
        self.speDefense = speDefense

