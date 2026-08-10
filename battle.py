"""This module contains the battle logic for the Pokemon game.
It handles the turn-based combat between two Pokemon, 
including calculating damage, applying type advantages, 
and determining the winner of the battle. """

import types_chart, moves, pokemon

num_of_pokemon_in_party = len(Character.party)
num_of_pokemon_in_party_fainted = 0
for i in range(0, num_of_pokemon_in_party):
    if Character.party[i].fainted:
        num_of_pokemon_in_party_fainted += 1
while num_of_pokemon_in_party_fainted < num_of_pokemon_in_party:
    # Battle logic goes here
    pass