from pokemon import *
import random
import inquirer

class Game:
    def __init__(self, time = 90):
        self.typePlayer = ''
        self.time = time
    
    def gameInit(self):
        self.optionUserCharac()
        self.optionBotCharac()


    def optionUserCharac(self):

        questions = [
            inquirer.List('elements',
                message="Which element do you want to choose?",
                choices=[Water.type, Grass.type, Fire.type],
                ),
            ]
        
        elements = inquirer.prompt(questions)
        self.typePlayer = elements
        
        if elements['elements'] == 'Water':
            self.selectionWater()
        
        if elements['elements'] == 'Grass':
            self.selectionGrass()
        
        if elements['elements'] == 'Fire':
            self.selectionFire()
    

    def optionBotCharac(self):

        elements = [Water.type, Grass.type, Fire.type]

        elementBot = random.choice(elements)

        if elementBot == 'Water':
            pokemons = ['Kyogre', 'Palkia', 'Blastoise']

            pokemonBot = random.choice(pokemons)

            self.theWaterPokemon(pokemons=None, pokemonBot=pokemonBot)
        
        if elementBot == 'Grass':
            pokemons = ['Zarude', 'Venusaur', 'Roserade']

            pokemonBot = random.choice(pokemons)

            self.theGrassPokemon(pokemons=None, pokemonBot=pokemonBot)
        
        if elementBot == 'Fire':
            pokemons = ['Reshiram', 'Charizard', 'Volcarona']

            pokemonBot = random.choice(pokemons)

            self.theFirePokemon(pokemons=None, pokemonBot=pokemonBot)


    
    def selectionWater(self):
            
        questions = [
        inquirer.List('pokemons',
            message="Which pokemon do you want to choose?",
            choices=['Kyogre', 'Palkia', 'Blastoise'],
            ),
        ]
        
        pokemons = inquirer.prompt(questions)

        self.theWaterPokemon(pokemons, pokemonBot=None)
    
    def selectionGrass(self):
            
        questions = [
        inquirer.List('pokemons',
            message="Which pokemon do you want to choose?",
            choices=['Zarude', 'Venusaur', 'Roserade'],
            ),
        ]
        
        pokemons = inquirer.prompt(questions)

        self.theGrassPokemon(pokemons, pokemonBot=None)
    
    def selectionFire(self):
            
        questions = [
        inquirer.List('pokemons',
            message="Which pokemon do you want to choose?",
            choices=['Reshiram', 'Charizard', 'Volcarona'],
            ),
        ]
        
        pokemons = inquirer.prompt(questions)

        self.theFirePokemon(pokemons, pokemonBot=None)
    
    def theWaterPokemon(self, pokemons, pokemonBot):

        water_pokemons = {
            "Kyogre": {"name": "Kyogre", "life": 770, "attack" : {'Blizzard': 100, 'Thunder': 110, 'To surf': 100}, 'defense': 90, 'speAttack': {'Water jet': 150, 'Waterfall': 140}, 'speDefense': 160, 'speed': 90},
            "Palkia": {"name": "Palkia", "life": 680, "attack" : {'Fire Blast': 140, 'Hydro pump': 130, 'Aqua Tail': 50}, 'defense': 100, 'speAttack': {'Draco Meteor': 150, 'Spacial Rend': 135}, 'speDefense': 120, 'speed': 120},
            "Blastoise": {"name": "Blastoise", "life": 630, "attack" : {'Water Gun': 122, 'Rapid Spin': 110, 'To surf': 100}, 'defense': 120, 'speAttack': {'Ice Beam': 150, 'Hydro Cannon': 140}, 'speDefense': 115, 'speed': 90}
        
        }

        water_pokemon_data = water_pokemons.get(pokemons['pokemons']) if pokemons else water_pokemons.get(pokemonBot)
        
        if water_pokemon_data:
            
            water_pokemon = Water(water_pokemon_data['name'], water_pokemon_data['life'], water_pokemon_data['attack'], water_pokemon_data['defense'], water_pokemon_data['speAttack'], water_pokemon_data['speDefense'], water_pokemon_data['speed'])

            if pokemons:
                print(f'Your pokemon: {water_pokemon.name} and have {water_pokemon.life} of life')
            elif pokemonBot:
                print(f'The pokemon of Bot: {water_pokemon.name} and have {water_pokemon.life} of life')

            water_pokemon.WaterPokes()

    
    def theGrassPokemon(self, pokemons, pokemonBot):

        if pokemons is not None and pokemons['pokemons'] == 'Zarude' or pokemonBot == 'Zarude':

            grass_pokemon = Grass("Zarude", 650, {'Multiple Whiplash': 115, 'Suction Vines': 100, 'Jungle Rage': 119}, 105, {'Leaf Guard': 150, 'Jungle Explosion': 145}, 120, 105)

            if pokemons:
                print(f'Your pokemon: {grass_pokemon.name} and have {grass_pokemon.life} of life')
            elif pokemonBot == 'Zarude':
                print(f'The pokemon of Bot: {grass_pokemon.name} and have {grass_pokemon.life} of life')

            grass_pokemon.GrassPokes()
        
        elif pokemons is not None and pokemons['pokemons'] == 'Venusaur' or pokemonBot == 'Venusaur':
            
            grass_pokemon = Grass("Venusaur", 780, {' Jungle Totem': 140, 'Dangerous Pollen': 130, 'Wobbly Loop': 100}, 100, {'Overgrow': 150, 'Sunshine': 130}, 160, 100)

            if pokemons:
                print(f'Your pokemon: {grass_pokemon.name} and have {grass_pokemon.life} of life')
            elif pokemonBot == 'Venusaur':
                print(f'The pokemon of Bot: {grass_pokemon.name} and have {grass_pokemon.life} of life')

            grass_pokemon.GrassPokes()
        
        elif pokemons is not None and pokemons['pokemons'] == 'Roserade' or pokemonBot == 'Roserade':
            
            grass_pokemon = Grass("Roserade", 630, {'Sweet Scent': 125, 'Poison Sting': 120, 'Petal Dance': 105}, 120, {'Energy Ball': 150, 'Solar Beam': 140}, 125, 90)

            if pokemons:
                print(f'Your pokemon: {grass_pokemon.name} and have {grass_pokemon.life} of life')
            elif pokemonBot == 'Roserade':
                print(f'The pokemon of Bot: {grass_pokemon.name} and have {grass_pokemon.life} of life')

            grass_pokemon.GrassPokes()
    

    def theFirePokemon(self, pokemons, pokemonBot):

        if pokemons is not None and pokemons['pokemons'] == 'Reshiram' or pokemonBot == 'Reshiram':

            fire_pokemon = Fire("Reshiram", 680, {'Flamethrower': 100, 'Fusion Flare': 110, 'Dragon Claw': 100}, 100, {'Turboblaze': 150, 'Blue Fire': 130}, 120, 90105)

            if pokemons:
                print(f'Your pokemon: {fire_pokemon.name} and have {fire_pokemon.life} of life')
            elif pokemonBot == 'Reshiram':
                print(f'The pokemon of Bot: {fire_pokemon.name} and have {fire_pokemon.life} of life')

            fire_pokemon.FirePokes()
        
        elif pokemons is not None and pokemons['pokemons'] == 'Charizard' or pokemonBot == 'Charizard':
            
            fire_pokemon = Fire("Charizard", 750, {'Slash': 140, 'Dragon breath': 130, 'Blaze': 90}, 100, {'Solar Power': 150, 'Hurricane Flame': 140}, 160, 120)

            if pokemons:
                print(f'Your pokemon: {fire_pokemon.name} and have {fire_pokemon.life} of life')
            elif pokemonBot == 'Charizard':
                print(f'The pokemon of Bot: {fire_pokemon.name} and have {fire_pokemon.life} of life')

            fire_pokemon.FirePokes()
        
        elif pokemons is not None and pokemons['pokemons'] == 'Volcarona' or pokemonBot == 'Volcarona':
            
            fire_pokemon = Fire("Volcarona", 650, {'Heat Wave': 122, 'Bug Buzz': 100, 'Fiery Dance': 80}, 95, {'Flame Body': 150, 'Flare Blitz': 150}, 105, 100)

            if pokemons:
                print(f'Your pokemon: {fire_pokemon.name} and have {fire_pokemon.life} of life')
            elif pokemonBot == 'Volcarona':
                print(f'The pokemon of Bot: {fire_pokemon.name} and have {fire_pokemon.life} of life')

            fire_pokemon.FirePokes()



game = Game()
game.gameInit()