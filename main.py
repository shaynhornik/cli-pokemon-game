# this is a rough start to sructure the opening scene and set initial variables

import io, sys, enum, random, pokemon



class Gender(enum.Enum):
    MALE = "boy"
    FEMALE = "girl"

class Character:
    def __init__(self, name, gender, party=None):
        self.name = name
        self.gender = gender
        self.party = party if party is not None else []


class Player(Character):
    def __init__(self, name, gender, party=None):
        super().__init__(name, gender, party)
        self.badges = []
        self.money = 0




print("Gotta code em all!"
"\nWelcome to the world of programming!"
"\nLet's embark on this exciting journey together!")
input("Press Enter to continue...")
name = input("\nBefore we begin, let's get to know you a little better."
      "\nWhat is your name?"
      "\nName: ")
print(f"\nNice to meet you, {name}!")
while True:
    gender_input = input("\nNow, are you a boy or a girl?"
      "\nGender: ").strip().lower()
    if gender_input in (Gender.MALE.value, Gender.FEMALE.value):
        gender = Gender(gender_input)
        break
    else:
        print("Invalid input. Please enter 'boy' or 'girl'.")

player = Player(name, gender)

print(f"\nGreat! So you're a {gender.value}, {name}!")

starter_pokemon = None

while True:

    print("\nNow, let's choose your first Pokemon!"
    "\nHere are the available options:"
    "\n1. Charmander"
    "\n2. Squirtle"
    "\n3. Bulbasaur"
    "\n4. Pikachu"
    "\n5. Eevee")
    choice = input("Please enter the number corresponding to your choice: ")

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

player.party.append(starter_pokemon)

print(f"\nCongratulations, {name}! You've chosen {starter_pokemon.name} as your first Pokemon!")

print("\nNow that you've chosen your starter Pokemon, it'e time to fight my grandson")

rival_name = input("\nWhat was his name again? ")

# start the battle with the grandson

rival_starter = None
if isinstance(starter_pokemon, pokemon.Charmander):
    rival_starter = pokemon.Squirtle()
elif isinstance(starter_pokemon, pokemon.Squirtle):
    rival_starter = pokemon.Bulbasaur()
elif isinstance(starter_pokemon, pokemon.Bulbasaur):
    rival_starter = pokemon.Charmander()
elif isinstance(starter_pokemon, pokemon.Pikachu):
    rival_starter = pokemon.Eevee()
elif isinstance(starter_pokemon, pokemon.Eevee):
    rival_starter = pokemon.Pikachu()
else:
    print("Error: Invalid starter Pokemon.")
    input("Press Enter to exit...")
    sys.exit()


rival = Character(rival_name, Gender.MALE, [rival_starter])

print(f"\nYour rival, {rival.name}, has chosen {rival_starter.name} as his starter Pokemon!")

print(f"\n{player.name} sent out {player.party[0].name}!")
print(f"{rival.name} sent out {rival.party[0].name}!")

player_current_pokemon = player.party[0]
rival_current_pokemon = rival.party[0]

turn_order = []
if player_current_pokemon.base_stats["Speed"] > rival_current_pokemon.base_stats["Speed"]:
    turn_order = [player, rival]
elif player_current_pokemon.base_stats["Speed"] < rival_current_pokemon.base_stats["Speed"]:
    turn_order = [rival, player]
else:
    luck = random.randint(0,1)
    if luck == 0:
        turn_order = [rival, player]
    else:
        turn_order = [player, rival]




