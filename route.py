#This module holds the wild pokemon that live in the tall grass on route 1.
import random, pokemon

ENCOUNTER_TABLE = [
    pokemon.Rattata,
    pokemon.Pidgey,
    pokemon.Caterpie,
    pokemon.Oddish,
    pokemon.Poliwag,
    pokemon.Growlithe,
    pokemon.Voltorb,
    pokemon.Mankey,
]

LOWEST_WILD_LEVEL = 3
HIGHEST_WILD_LEVEL = 7


def random_encounter():
    which_one = random.choice(ENCOUNTER_TABLE)
    #the table holds the classes themselves so I have to call it to get a pokemon
    wild_pokemon = which_one()
    wild_level = random.randint(LOWEST_WILD_LEVEL, HIGHEST_WILD_LEVEL)
    pokemon.set_level(wild_pokemon, wild_level)
    return wild_pokemon
