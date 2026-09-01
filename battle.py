"""This module contains the battle logic for the Pokemon game.
It handles the turn-based combat between two Pokemon, 
including calculating damage, applying type advantages, 
and determining the winner of the battle. """

import random, types_chart, moves, pokemon

PARTY_SIZE_LIMIT = 6
# the real formula was giving me like 4 damage a hit and the battles took forever,
# so I multiply the damage by this at the end. Any higher than this and a super
# effective hit from a matching type takes something out in one shot
DAMAGE_MULTIPLIER = 2.0
LEVEL_GAP_THAT_STILL_COUNTS = 5


def print_hp_bar(a_pokemon):
    max_hp = a_pokemon.base_stats["HP"]
    current_hp = a_pokemon.current_stats["HP"]
    if current_hp < 0:
        current_hp = 0
    number_of_blocks = int((current_hp / max_hp) * 20)
    bar = ""
    for i in range(0, 20):
        if i < number_of_blocks:
            bar = bar + "#"
        else:
            bar = bar + "-"
    print(f"{a_pokemon.name} (Lv {a_pokemon.level}) [{bar}] {current_hp}/{max_hp}")


def damage_calc(attacker, defender, move_name):
    move = moves.MOVES[move_name]
    power = move["power"]
    attack = attacker.current_stats["Attack"]
    defense = defender.current_stats["Defense"]
    level = attacker.level
    #this is a squished down version of the real pokemon damage formula
    base_damage = (((((2 * level) / 5) + 2) * power * (attack / defense)) / 50) + 2
    effectiveness = types_chart.get_effectiveness(move["type"], defender.type)
    same_type_bonus = 1.0
    if move["type"] == attacker.type:
        same_type_bonus = 1.5
    luck = random.uniform(0.85, 1.0)
    total_damage = base_damage * effectiveness * same_type_bonus * luck * DAMAGE_MULTIPLIER
    total_damage = int(total_damage)
    if total_damage < 1:
        total_damage = 1
    return total_damage, effectiveness


def does_it_hit(move_name):
    move = moves.MOVES[move_name]
    roll = random.randint(1, 100)
    if roll <= move["accuracy"]:
        return True
    else:
        return False


def do_attack(attacker, defender, move_name):
    print(f"\n{attacker.name} used {move_name.title()}!")
    if does_it_hit(move_name) == False:
        print(f"{attacker.name}'s attack missed!")
        return
    damage, effectiveness = damage_calc(attacker, defender, move_name)
    defender.current_stats["HP"] = defender.current_stats["HP"] - damage
    if effectiveness > types_chart.neutral:
        print("It's super effective!")
    elif effectiveness < types_chart.neutral:
        print("It's not very effective...")
    print(f"{defender.name} took {damage} damage.")
    if defender.current_stats["HP"] <= 0:
        defender.current_stats["HP"] = 0
        defender.fainted = True
        print(f"{defender.name} fainted!")


def choose_move(a_pokemon):
    while True:
        print(f"\nWhat should {a_pokemon.name} do?")
        for i in range(0, len(a_pokemon.moves)):
            move_name = a_pokemon.moves[i]
            move = moves.MOVES[move_name]
            print(f"{i + 1}. {move_name.title()} - {move['type'].value}, power {move['power']}")
        choice = input("Pick a move: ").strip()
        if choice.isdigit() == False:
            print("Invalid input. Please enter a number.")
            continue
        choice_as_a_number = int(choice)
        if choice_as_a_number < 1 or choice_as_a_number > len(a_pokemon.moves):
            print("Invalid input. That isn't one of the moves.")
            continue
        return a_pokemon.moves[choice_as_a_number - 1]


def choose_pokemon(player, current_pokemon, can_go_back):
    pokemon_that_can_fight = []
    for i in range(0, len(player.party)):
        if player.party[i].fainted == False and player.party[i] != current_pokemon:
            pokemon_that_can_fight.append(player.party[i])
    if len(pokemon_that_can_fight) == 0:
        print("\nYou don't have anyone else to send out!")
        return None
    while True:
        print("\nWho should go in?")
        for i in range(0, len(pokemon_that_can_fight)):
            one_of_them = pokemon_that_can_fight[i]
            print(f"{i + 1}. {one_of_them.name} (Lv {one_of_them.level}) HP: {one_of_them.current_stats['HP']}/{one_of_them.base_stats['HP']}")
        if can_go_back == True:
            print("0. Never mind")
        choice = input("Pick a number: ").strip()
        if choice == "0" and can_go_back == True:
            return None
        if choice.isdigit() == False:
            print("Invalid input. Please enter a number.")
            continue
        choice_as_a_number = int(choice)
        if choice_as_a_number < 1 or choice_as_a_number > len(pokemon_that_can_fight):
            print("Invalid input. That isn't one of your pokemon.")
            continue
        return pokemon_that_can_fight[choice_as_a_number - 1]


def try_to_catch(wild_pokemon):
    max_hp = wild_pokemon.base_stats["HP"]
    current_hp = wild_pokemon.current_stats["HP"]
    how_much_hp_is_left = current_hp / max_hp
    #the more beat up it is the better the odds are
    catch_chance = ((1 - how_much_hp_is_left) * 70) + 15
    roll = random.randint(1, 100)
    if roll <= catch_chance:
        return True
    else:
        return False


def try_to_run(player_pokemon, wild_pokemon):
    if player_pokemon.current_stats["Speed"] >= wild_pokemon.current_stats["Speed"]:
        return True
    elif random.randint(1, 100) <= 40:
        return True
    else:
        return False


# this returns a string so that main.py knows what happened. it can be
# "win", "lose", "caught" or "ran"
def battle(player, opponent_name, opponent_party, is_wild_battle):
    print("\n============ BATTLE ============")
    opponent_current_pokemon = opponent_party[0]
    if is_wild_battle == True:
        print(f"A wild {opponent_current_pokemon.name} appeared!")
    else:
        print(f"{opponent_name} wants to fight!")
        print(f"{opponent_name} sent out {opponent_current_pokemon.name}!")

    player_current_pokemon = None
    for i in range(0, len(player.party)):
        if player.party[i].fainted == False:
            player_current_pokemon = player.party[i]
            break
    if player_current_pokemon == None:
        print("All of your pokemon have fainted! You can't fight right now.")
        return "lose"
    print(f"{player.name} sent out {player_current_pokemon.name}!")

    while True:
        print("\n--------------------------------")
        print_hp_bar(opponent_current_pokemon)
        print_hp_bar(player_current_pokemon)

        player_move = None
        the_player_is_attacking = False
        while True:
            print("\n1. Fight")
            print("2. Switch Pokemon")
            if is_wild_battle == True:
                print("3. Throw a Pokeball")
                print("4. Run away")
            choice = input("What do you want to do? ").strip()

            if choice == "1":
                player_move = choose_move(player_current_pokemon)
                the_player_is_attacking = True
                break
            elif choice == "2":
                switched_to = choose_pokemon(player, player_current_pokemon, True)
                if switched_to == None:
                    continue
                player_current_pokemon = switched_to
                print(f"\n{player.name} sent out {player_current_pokemon.name}!")
                break
            elif choice == "3" and is_wild_battle == True:
                if len(player.party) >= PARTY_SIZE_LIMIT:
                    print("\nYour party is full! You can't carry any more pokemon.")
                    continue
                print("\nYou threw a Pokeball...")
                if try_to_catch(opponent_current_pokemon) == True:
                    print(f"Gotcha! {opponent_current_pokemon.name} was caught!")
                    player.party.append(opponent_current_pokemon)
                    return "caught"
                else:
                    print(f"Oh no! {opponent_current_pokemon.name} broke free!")
                    break
            elif choice == "4" and is_wild_battle == True:
                if try_to_run(player_current_pokemon, opponent_current_pokemon) == True:
                    print("\nYou got away safely!")
                    return "ran"
                else:
                    print("\nYou couldn't get away!")
                    break
            else:
                print("Invalid input. Please pick one of the options.")

        opponent_move = random.choice(opponent_current_pokemon.moves)

        # if the player switched or threw a ball then that was their whole turn,
        # so the other pokemon is the only one that gets to attack
        turn_order = []
        if the_player_is_attacking == False:
            turn_order = ["opponent"]
        elif player_current_pokemon.current_stats["Speed"] > opponent_current_pokemon.current_stats["Speed"]:
            turn_order = ["player", "opponent"]
        elif player_current_pokemon.current_stats["Speed"] < opponent_current_pokemon.current_stats["Speed"]:
            turn_order = ["opponent", "player"]
        else:
            luck = random.randint(0, 1)
            if luck == 0:
                turn_order = ["opponent", "player"]
            else:
                turn_order = ["player", "opponent"]

        for i in range(0, len(turn_order)):
            if turn_order[i] == "player":
                do_attack(player_current_pokemon, opponent_current_pokemon, player_move)
            else:
                do_attack(opponent_current_pokemon, player_current_pokemon, opponent_move)
            if opponent_current_pokemon.fainted == True or player_current_pokemon.fainted == True:
                break

        if opponent_current_pokemon.fainted == True:
            # I dont want a level 30 pokemon getting a whole level for stomping a
            # level 4 rattata, so the thing you beat has to be somewhere near you
            if opponent_current_pokemon.level + LEVEL_GAP_THAT_STILL_COUNTS >= player_current_pokemon.level:
                pokemon.level_up(player_current_pokemon)
                print(f"{player_current_pokemon.name} grew to level {player_current_pokemon.level}!")
            else:
                print(f"{player_current_pokemon.name} didn't learn much from that one.")
            the_next_one = None
            for i in range(0, len(opponent_party)):
                if opponent_party[i].fainted == False:
                    the_next_one = opponent_party[i]
                    break
            if the_next_one == None:
                if is_wild_battle == False:
                    print(f"\n{opponent_name} is out of usable pokemon!")
                    print(f"{player.name} won the battle!")
                return "win"
            opponent_current_pokemon = the_next_one
            print(f"\n{opponent_name} sent out {opponent_current_pokemon.name}!")
            input("Press Enter to continue...")
            continue

        if player_current_pokemon.fainted == True:
            the_next_one = choose_pokemon(player, player_current_pokemon, False)
            if the_next_one == None:
                print(f"\n{player.name} is out of usable pokemon!")
                print(f"{player.name} blacked out!")
                return "lose"
            player_current_pokemon = the_next_one
            print(f"\n{player.name} sent out {player_current_pokemon.name}!")
