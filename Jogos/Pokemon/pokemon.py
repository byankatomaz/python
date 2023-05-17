class Pokemon():
    def __init__(self, name, attack, defense, speed):
        self.type = ''
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed


class Water(Pokemon):
    type = 'Water'
    def __init__(self, name, life, attack, defense, speAttack, speDefense, speed):
        super().__init__(name, attack, defense, speed)
        self.life = life
        self.speAttack = speAttack
        self.speDefense = speDefense


class Grass(Pokemon):
    type = 'Grass'
    def __init__(self, name, life, attack, defense, speAttack, speDefense, speed):
        super().__init__(name, attack, defense, speed)
        self.life = life
        self.speAttack = speAttack
        self.speDefense = speDefense
    

class Fire(Pokemon):
    type = 'Fire'
    def __init__(self, name, life, attack, defense, speAttack, speDefense, speed):
        super().__init__(name, attack, defense, speed)
        self.life = life
        self.speAttack = speAttack
        self.speDefense = speDefense
    
