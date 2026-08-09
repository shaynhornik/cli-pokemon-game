# this is a rough start to sructure the opening scene and set initial variables

import io, sys, enum


class Gender(enum.Enum):
    MALE = "boy"
    FEMALE = "girl"

class Character:
    def __init__(self, name, gender, party=None):
        self.name = name
        self.gender = gender
        self.party = party


class Player(Character):
    def __init__(self, name, gender, party=None):
        super().__init__()


class Pokemon:
    def __init__ (self, name, type, moves, base_stats, level):
        self.name = name
        self.type = type
        self.moves = moves
        self.base_stats = base_stats
        self.level = level

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "fire", ["scratch", "ember"], {"HP": 39, "Attack": 52, "Defense": 43, "Speed": 65}, 5)

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "water", ["tackle", "water gun"], {"HP": 44, "Attack": 48, "Defense": 65, "Speed": 43}, 5)

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", "grass", ["tackle", "vine whip"], {"HP": 45, "Attack": 49, "Defense": 49, "Speed": 45}, 5)

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "electric", ["thunder shock", "quick attack"], {"HP": 35, "Attack": 55, "Defense": 40, "Speed": 90}, 5)

class Eevee(Pokemon):
    def __init__(self):
        super().__init__("Eevee", "normal", ["tackle", "quick attack"], {"HP": 55, "Attack": 55, "Defense": 50, "Speed": 55}, 5)    

class Starter(enum.Enum):
    CHARMANDER = 1
    SQUIRTLE = 2
    BULBASAUR = 3
    PIKACHU = 4
    EEVEE = 5

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
        starter_pokemon = Charmander()
        break
    elif choice == "2":
        starter_pokemon = Squirtle()
        break
    elif choice == "3":
        starter_pokemon = Bulbasaur()
        break
    elif choice == "4":
        starter_pokemon = Pikachu()
        break
    elif choice == "5":
        starter_pokemon = Eevee()
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

# start the battle with the grandson


