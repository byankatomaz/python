from pokemon import *
import random
import inquirer

class Game:
    def __init__(self):
        self.typePlayer = ''
        self.typeBot = ''
        self.data_pokemons = []
        self.cont = 0
    
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
        self.typePlayer = elements['elements']
        
        if elements['elements'] == 'Water':
            self.selectionWater()
        
        elif elements['elements'] == 'Grass':
            self.selectionGrass()
        
        elif elements['elements'] == 'Fire':
            self.selectionFire()

        return self.typePlayer

    def optionBotCharac(self):

        elements = [Water.type, Grass.type, Fire.type]
        elementBot = random.choice(elements)

        self.typeBot = elementBot

        if elementBot == 'Water':
            pokemons = ['Kyogre', 'Palkia', 'Blastoise']
            pokemonBot = random.choice(pokemons)

            self.theWaterPokemon(pokemons=None, pokemonBot=pokemonBot)
        
        elif elementBot == 'Grass':
            pokemons = ['Zarude', 'Venusaur', 'Roserade']
            pokemonBot = random.choice(pokemons)

            self.theGrassPokemon(pokemons=None, pokemonBot=pokemonBot)
        
        elif elementBot == 'Fire':
            pokemons = ['Reshiram', 'Charizard', 'Volcarona']
            pokemonBot = random.choice(pokemons)

            self.theFirePokemon(pokemons=None, pokemonBot=pokemonBot)

        return self.typeBot
    
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

        if pokemons is not None:
            water_pokemon_data = water_pokemons.get(pokemons['pokemons'])

            water_pokemon = Water(water_pokemon_data['name'], water_pokemon_data['life'], water_pokemon_data['attack'], water_pokemon_data['defense'], water_pokemon_data['speAttack'], water_pokemon_data['speDefense'], water_pokemon_data['speed'])
            self.data_pokemons.append(water_pokemon)

            print(f'Your pokemon: {water_pokemon.name}, of type {Water.type} and have {water_pokemon.life} of life')
            self.cont += 1

        else:
            water_pokemon_data_bot = water_pokemons.get(pokemonBot)

            water_pokemon_bot = Water(water_pokemon_data_bot['name'], water_pokemon_data_bot['life'], water_pokemon_data_bot['attack'], water_pokemon_data_bot['defense'], water_pokemon_data_bot['speAttack'], water_pokemon_data_bot['speDefense'], water_pokemon_data_bot['speed'])
            self.data_pokemons.append(water_pokemon_bot)

            print(f'The pokemon of Bot: {water_pokemon_bot.name}, of type {Water.type} and have {water_pokemon_bot.life} of life')
            self.cont += 1

        if self.cont == 2:
            return self.data_pokemons

    
    
    def theGrassPokemon(self, pokemons, pokemonBot):

        grass_pokemons = {
            "Zarude": {"name": "Zarude", "life": 650, "attack" : {'Multiple Whiplash': 115, 'Suction Vines': 100, 'Jungle Rage': 119}, 'defense': 105, 'speAttack': {'Leaf Guard': 150, 'Jungle Explosion': 145}, 'speDefense': 120, 'speed': 105},
            "Venusaur": {"name": "Venusaur", "life": 780, "attack" :{' Jungle Totem': 140, 'Dangerous Pollen': 130, 'Wobbly Loop': 100}, 'defense': 100, 'speAttack': {'Overgrow': 150, 'Sunshine': 130}, 'speDefense': 160, 'speed': 100},
            "Roserade": {"name": "Roserade", "life": 630, "attack" : {'Sweet Scent': 125, 'Poison Sting': 120, 'Petal Dance': 105}, 'defense': 120, 'speAttack': {'Energy Ball': 150, 'Solar Beam': 140}, 'speDefense': 125, 'speed': 90}
        }

        if pokemons is not None:
            grass_pokemon_data = grass_pokemons.get(pokemons['pokemons'])

            grass_pokemon = Grass(grass_pokemon_data['name'], grass_pokemon_data['life'], grass_pokemon_data['attack'], grass_pokemon_data['defense'], grass_pokemon_data['speAttack'], grass_pokemon_data['speDefense'], grass_pokemon_data['speed'])
            self.data_pokemons.append(grass_pokemon)
            
            print(f'Your pokemon: {grass_pokemon.name}, of type {Grass.type} and have {grass_pokemon.life} of life')
            self.cont += 1

        else:
            grass_pokemon_data_bot = grass_pokemons.get(pokemonBot)

            grass_pokemon_bot = Grass(grass_pokemon_data_bot['name'], grass_pokemon_data_bot['life'], grass_pokemon_data_bot['attack'], grass_pokemon_data_bot['defense'], grass_pokemon_data_bot['speAttack'], grass_pokemon_data_bot['speDefense'], grass_pokemon_data_bot['speed'])
            self.data_pokemons.append(grass_pokemon_bot)

            print(f'The pokemon of Bot: {grass_pokemon_bot.name}, of type {Grass.type} and have {grass_pokemon_bot.life} of life')
            self.cont += 1

        if self.cont == 2:
            return self.data_pokemons


    def theFirePokemon(self, pokemons, pokemonBot):

        fire_pokemons = {
            "Reshiram": {"name": "Reshiram", "life": 680, "attack" : {'Flamethrower': 100, 'Fusion Flare': 110, 'Dragon Claw': 100}, 'defense': 100, 'speAttack': {'Turboblaze': 150, 'Blue Fire': 130}, 'speDefense': 120, 'speed': 90},
            "Charizard": {"name": "Charizard", "life": 750, "attack" : {'Slash': 140, 'Dragon breath': 130, 'Blaze': 90}, 'defense': 100, 'speAttack': {'Solar Power': 150, 'Hurricane Flame': 140}, 'speDefense': 160, 'speed': 120},
            "Volcarona": {"name": "Volcarona", "life": 650, "attack" : {'Heat Wave': 122, 'Bug Buzz': 100, 'Fiery Dance': 80}, 'defense': 95, 'speAttack': {'Flame Body': 150, 'Flare Blitz': 150}, 'speDefense': 105, 'speed': 100}
        }

        if pokemons is not None:
            fire_pokemon_data = fire_pokemons.get(pokemons['pokemons'])

            fire_pokemon = Fire(fire_pokemon_data['name'], fire_pokemon_data['life'], fire_pokemon_data['attack'], fire_pokemon_data['defense'], fire_pokemon_data['speAttack'], fire_pokemon_data['speDefense'], fire_pokemon_data['speed'])
            self.data_pokemons.append(fire_pokemon)
            
            print(f'Your pokemon: {fire_pokemon.name}, of type {Fire.type} and have {fire_pokemon.life} of life')
            self.cont += 1

        else:
            fire_pokemon_data_bot = fire_pokemons.get(pokemonBot)

            fire_pokemon_bot = Fire(fire_pokemon_data_bot['name'], fire_pokemon_data_bot['life'], fire_pokemon_data_bot['attack'], fire_pokemon_data_bot['defense'], fire_pokemon_data_bot['speAttack'], fire_pokemon_data_bot['speDefense'], fire_pokemon_data_bot['speed'])
            self.data_pokemons.append(fire_pokemon_bot)
            
            print(f'The pokemon of Bot: {fire_pokemon_bot.name}, of type {Fire.type} and have {fire_pokemon_bot.life} of life')
            self.cont += 1
        
        if self.cont == 2:
            return self.data_pokemons


if __name__ == '__main__':
    
    game = Game()
    game.gameInit()
