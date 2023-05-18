class Pokemon():
    def __init__(self, name, life, attack, defense, speAttack, speDefense, speed):
        self.type = ''
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.life = life
        self.speAttack = speAttack
        self.speDefense = speDefense


class Water(Pokemon):
    type = 'Water'
    def __init__(self, name, life, attack, defense, speAttack, speDefense, speed):
        super().__init__(name, life, attack, defense, speAttack, speDefense, speed)


class Grass(Pokemon):
    type = 'Grass'
    def __init__(self, name, life, attack, defense, speAttack, speDefense, speed):
        super().__init__(name, life, attack, defense, speAttack, speDefense, speed)
    

class Fire(Pokemon):
    type = 'Fire'
    def __init__(self, name, life, attack, defense, speAttack, speDefense, speed):
        super().__init__(name, life, attack, defense, speAttack, speDefense, speed)
