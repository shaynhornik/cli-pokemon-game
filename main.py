# this is a rough start to sructure the opening scene and set initial variables
# its not so rough anymore, the whole game runs out of here now

import io, sys, enum, random, pokemon, character, battle, route


def opening_scene():
    print("Gotta code em all!"
    "\nWelcome to the world of programming!"
    "\nLet's embark on this exciting journey together!")
    input("Press Enter to continue...")
    name = input("\nBefore we begin, let's get to know you a little better."
          "\nWhat is your name?"
          "\nName: ").strip()
    if name == "":
        name = "Red"
        print("\nYou didn't type anything so I'm going to call you Red.")
    print(f"\nNice to meet you, {name}!")
    while True:
        gender_input = input("\nNow, are you a boy or a girl?"
          "\nGender: ").strip().lower()
        if gender_input in (character.Gender.MALE.value, character.Gender.FEMALE.value):
            gender = character.Gender(gender_input)
            break
        else:
            print("Invalid input. Please enter 'boy' or 'girl'.")
    print(f"\nGreat! So you're a {gender.value}, {name}!")
    return character.Player(name, gender)


def pick_your_starter():
    starter_pokemon = None
    while True:

        print("\nNow, let's choose your first Pokemon!"
        "\nHere are the available options:"
        "\n1. Charmander"
        "\n2. Squirtle"
        "\n3. Bulbasaur"
        "\n4. Pikachu"
        "\n5. Eevee")
        choice = input("Please enter the number corresponding to your choice: ").strip()

        if choice == "1":
            starter_pokemon = pokemon.Charmander()
            break
        elif choice == "2":
            starter_pokemon = pokemon.Squirtle()
            break
        elif choice == "3":
            starter_pokemon = pokemon.Bulbasaur()
            break
        elif choice == "4":
            starter_pokemon = pokemon.Pikachu()
            break
        elif choice == "5":
            starter_pokemon = pokemon.Eevee()
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

    if starter_pokemon == None:
        print("No starter Pokemon selected. You broke the game.")
        input("Press Enter to exit...")
        sys.exit()

    return starter_pokemon


# He grabs the leftover one, so you have the type advantage on him. I had this
# backwards at first and he picked the one that beats yours, but then he always
# has a super effective move and you literally can not win the first fight
def pick_the_rivals_starter(starter_pokemon):
    rival_starter = None
    if isinstance(starter_pokemon, pokemon.Charmander):
        rival_starter = pokemon.Bulbasaur()
    elif isinstance(starter_pokemon, pokemon.Squirtle):
        rival_starter = pokemon.Charmander()
    elif isinstance(starter_pokemon, pokemon.Bulbasaur):
        rival_starter = pokemon.Squirtle()
    elif isinstance(starter_pokemon, pokemon.Pikachu):
        rival_starter = pokemon.Squirtle()
    elif isinstance(starter_pokemon, pokemon.Eevee):
        rival_starter = pokemon.Pikachu()
    else:
        print("Error: Invalid starter Pokemon.")
        input("Press Enter to exit...")
        sys.exit()
    return rival_starter


# for the rematch he shows up with the thing that beats your starter, because
# he has had the whole game to go find one
def pick_his_rematch_starter(starter_pokemon):
    rematch_starter = None
    if isinstance(starter_pokemon, pokemon.Charmander):
        rematch_starter = pokemon.Squirtle()
    elif isinstance(starter_pokemon, pokemon.Squirtle):
        rematch_starter = pokemon.Bulbasaur()
    elif isinstance(starter_pokemon, pokemon.Bulbasaur):
        rematch_starter = pokemon.Charmander()
    elif isinstance(starter_pokemon, pokemon.Pikachu):
        rematch_starter = pokemon.Eevee()
    elif isinstance(starter_pokemon, pokemon.Eevee):
        rematch_starter = pokemon.Pikachu()
    else:
        print("Error: Invalid starter Pokemon.")
        input("Press Enter to exit...")
        sys.exit()
    return rematch_starter


def show_the_party(player):
    print("\n=========== YOUR PARTY ==========")
    for i in range(0, len(player.party)):
        one_of_them = player.party[i]
        status = "OK"
        if one_of_them.fainted == True:
            status = "FAINTED"
        print(f"{i + 1}. {one_of_them.name} (Lv {one_of_them.level}) {one_of_them.type.value}")
        print(f"   HP: {one_of_them.current_stats['HP']}/{one_of_them.base_stats['HP']} - {status}")
        print(f"   Moves: {', '.join(one_of_them.moves)}")
    print("=================================")
    input("Press Enter to continue...")


def anybody_is_hurt(player):
    for i in range(0, len(player.party)):
        one_of_them = player.party[i]
        if one_of_them.fainted == True:
            return True
        if one_of_them.current_stats["HP"] < one_of_them.base_stats["HP"]:
            return True
    return False


def pokemon_center(player):
    print("\nYou walk into the Pokemon Center."
    "\nNurse Joy takes your pokemon and puts them in the machine...")
    character.heal_party(player)
    print("We hope to see you again!")
    print("Your whole party is back to full health.")
    input("Press Enter to continue...")


def walk_in_the_tall_grass(player):
    if character.has_a_pokemon_that_can_fight(player) == False:
        print("\nAll of your pokemon have fainted. You should go heal up first.")
        input("Press Enter to continue...")
        return
    print("\nYou walk into the tall grass...")
    wild_pokemon = route.random_encounter()
    what_happened = battle.battle(player, wild_pokemon.name, [wild_pokemon], True)
    if what_happened == "caught":
        print(f"{wild_pokemon.name} was added to your party! You have {len(player.party)} pokemon now.")
    elif what_happened == "win":
        print(f"\nThe wild {wild_pokemon.name} ran off into the grass.")
    elif what_happened == "lose":
        print("\nYou scramble back to the Pokemon Center...")
        character.heal_party(player)
        print("Your party has been healed.")
    input("Press Enter to continue...")


def the_final_battle(player, rival):
    if len(player.party) < 2:
        print(f"\n{rival.name} is waiting for you at the north end of the route."
        "\nHe laughs at you. 'You want to fight me with ONE pokemon?'"
        "\nYou should probably go catch a few more first.")
        input("Press Enter to continue...")
        return False
    if character.has_a_pokemon_that_can_fight(player) == False:
        print("\nAll of your pokemon have fainted. You should go heal up first.")
        input("Press Enter to continue...")
        return False

    # I kept wandering into this fight with half my team knocked out
    if anybody_is_hurt(player) == True:
        print("\nYour team is still beat up from the last fight.")
        answer = input("Do you want to go fight him anyway? (yes/no) ").strip().lower()
        if answer != "yes" and answer != "y":
            print("You turn around and head back toward the Pokemon Center.")
            input("Press Enter to continue...")
            return False

    print(f"\nYou walk north and {rival.name} is standing in the middle of the path.")
    print("'I've been training this whole time. Let's see what you've got!'")
    print("He's got a pokemon with him that you have a bad feeling about.")
    input("Press Enter to continue...")

    # he gets a full team for the rematch. I build it fresh off of your
    # best pokemon every time, otherwise he sits at the same level forever and
    # you either steamroll him or you can never touch him
    #6 is the floor so he isn't a pushover if you run straight at him. I tried
    # using the average of your party but your main pokemon is always way above
    # the average so he never stood a chance.
    # I only work this out the FIRST time you walk up to him and then I save it on
    # him, because if I redo it every attempt he levels up right along with you and
    # then training after you lose does literally nothing
    if rival.rematch_level == 0:
        your_best_level = 6
        for i in range(0, len(player.party)):
            if player.party[i].level > your_best_level:
                your_best_level = player.party[i].level
        rival.rematch_level = your_best_level
    your_best_level = rival.rematch_level

    # he also brings one less pokemon than you have. fighting three of his with
    # two of mine was basically impossible no matter how much I trained
    how_many_he_brings = len(player.party) - 1
    if how_many_he_brings > 3:
        how_many_he_brings = 3
    if how_many_he_brings < 1:
        how_many_he_brings = 1

    rival.party = [pick_his_rematch_starter(player.party[0])]
    # his starter matches your best pokemon and the rest of his team fills in
    # under it. I had his starter 2 levels over you for a while but with a type
    # advantage on top of that it was unbeatable if you only had 2 pokemon
    pokemon.set_level(rival.party[0], your_best_level)
    if how_many_he_brings >= 2:
        rival.party.append(pokemon.set_level(pokemon.Pidgey(), your_best_level - 1))
    if how_many_he_brings >= 3:
        rival.party.append(pokemon.set_level(pokemon.Rattata(), your_best_level))
    character.heal_party(rival)

    what_happened = battle.battle(player, rival.name, rival.party, False)
    if what_happened == "win":
        print("\n============ THE END ============")
        print(f"{rival.name} stares at the ground for a second and then grins."
        f"\n'Alright {player.name}, you win. You're not bad after all.'"
        "\nHe hands you a Town Map and runs off toward the next city."
        "\n\nYou did it. You beat your rival with the team you raised yourself."
        "\nThanks for playing!")
        print("=================================")
        show_the_party(player)
        return True
    else:
        print(f"\n{rival.name} laughs. 'Smell ya later!'")
        print("You drag yourself back to the Pokemon Center to try again."
        "\nMaybe go train in the tall grass, or catch a couple more pokemon first.")
        character.heal_party(player)
        # he shouldnt keep the whole team stacked up every time I lose to him
        rival.party = [rival.party[0]]
        input("Press Enter to continue...")
        return False


def overworld(player, rival):
    while True:
        print("\n============ ROUTE 1 ============")
        print("1. Walk in the tall grass")
        print("2. Go to the Pokemon Center")
        print("3. Check your party")
        print(f"4. Go challenge {rival.name}")
        print("5. Quit the game")
        choice = input("What do you want to do? ").strip()

        if choice == "1":
            walk_in_the_tall_grass(player)
        elif choice == "2":
            pokemon_center(player)
        elif choice == "3":
            show_the_party(player)
        elif choice == "4":
            you_won = the_final_battle(player, rival)
            if you_won == True:
                return
        elif choice == "5":
            print("\nThanks for playing!")
            return
        else:
            print("Invalid input. Please enter a number between 1 and 5.")


def main():
    player = opening_scene()

    starter_pokemon = pick_your_starter()
    player.party.append(starter_pokemon)
    print(f"\nCongratulations, {player.name}! You've chosen {starter_pokemon.name} as your first Pokemon!")

    print("\nNow that you've chosen your starter Pokemon, it'e time to fight my grandson")
    rival_name = input("\nWhat was his name again? ").strip()
    if rival_name == "":
        rival_name = "Blue"

    rival_starter = pick_the_rivals_starter(starter_pokemon)
    rival = character.Character(rival_name, character.Gender.MALE, [rival_starter])
    #this gets filled in the first time you challenge him on the route
    rival.rematch_level = 0
    print(f"\nYour rival, {rival.name}, has chosen {rival_starter.name} as his starter Pokemon!")
    input("Press Enter to continue...")

    what_happened = battle.battle(player, rival.name, rival.party, False)
    if what_happened == "win":
        print(f"\n{rival.name} recalls his pokemon. 'Whatever! I was going easy on you!'")
    else:
        print(f"\n{rival.name} laughs at you. 'Is that all you've got?'")
        print("Your mom finds you on the floor of the lab and heals your pokemon.")
    character.heal_party(player)
    character.heal_party(rival)
    input("Press Enter to continue...")

    print("\nYou step outside onto Route 1."
    "\nThere is tall grass everywhere and a Pokemon Center on the corner."
    f"\n{rival.name} took off north to train.")

    overworld(player, rival)


if __name__ == "__main__":
    main()
