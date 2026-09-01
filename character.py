import enum, pokemon

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


def heal_party(a_character):
    for i in range(0, len(a_character.party)):
        pokemon.full_heal(a_character.party[i])


def has_a_pokemon_that_can_fight(a_character):
    for i in range(0, len(a_character.party)):
        if a_character.party[i].fainted == False:
            return True
    return False
