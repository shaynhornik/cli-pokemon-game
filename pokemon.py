import enum, types_chart

class Pokemon:
    def __init__ (self, name, type, moves, base_stats, level):
        self.name = name
        self.type = type
        self.moves = moves
        self.base_stats = base_stats
        self.level = level
        self.current_stats = base_stats.copy()
        self.fainted = False

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", types_chart.Type.FIRE, ["scratch", "ember"], {"HP": 39, "Attack": 52, "Defense": 43, "Speed": 65}, 5)

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", types_chart.Type.WATER, ["tackle", "water gun"], {"HP": 44, "Attack": 48, "Defense": 65, "Speed": 43}, 5)

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", types_chart.Type.GRASS, ["tackle", "vine whip"], {"HP": 45, "Attack": 49, "Defense": 49, "Speed": 45}, 5)

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", types_chart.Type.ELECTRIC, ["thunder shock", "quick attack"], {"HP": 35, "Attack": 55, "Defense": 40, "Speed": 90}, 5)

class Eevee(Pokemon):
    def __init__(self):
        super().__init__("Eevee", types_chart.Type.NORMAL, ["tackle", "quick attack"], {"HP": 55, "Attack": 55, "Defense": 50, "Speed": 55}, 5)    

# these are the ones that show up in the tall grass. they all start at level 3
# and then the route module levels them up to whatever it wants them to be
class Rattata(Pokemon):
    def __init__(self):
        super().__init__("Rattata", types_chart.Type.NORMAL, ["tackle", "quick attack"], {"HP": 30, "Attack": 56, "Defense": 35, "Speed": 72}, 3)

class Pidgey(Pokemon):
    def __init__(self):
        super().__init__("Pidgey", types_chart.Type.NORMAL, ["gust", "quick attack"], {"HP": 40, "Attack": 45, "Defense": 40, "Speed": 56}, 3)

class Caterpie(Pokemon):
    def __init__(self):
        super().__init__("Caterpie", types_chart.Type.GRASS, ["tackle", "absorb"], {"HP": 45, "Attack": 30, "Defense": 35, "Speed": 45}, 3)

class Oddish(Pokemon):
    def __init__(self):
        super().__init__("Oddish", types_chart.Type.GRASS, ["absorb", "razor leaf"], {"HP": 45, "Attack": 50, "Defense": 55, "Speed": 30}, 3)

class Poliwag(Pokemon):
    def __init__(self):
        super().__init__("Poliwag", types_chart.Type.WATER, ["bubble", "water gun"], {"HP": 40, "Attack": 50, "Defense": 40, "Speed": 90}, 3)

class Growlithe(Pokemon):
    def __init__(self):
        super().__init__("Growlithe", types_chart.Type.FIRE, ["ember", "headbutt"], {"HP": 55, "Attack": 70, "Defense": 45, "Speed": 60}, 3)

class Voltorb(Pokemon):
    def __init__(self):
        super().__init__("Voltorb", types_chart.Type.ELECTRIC, ["tackle", "spark"], {"HP": 40, "Attack": 30, "Defense": 50, "Speed": 100}, 3)

class Mankey(Pokemon):
    def __init__(self):
        super().__init__("Mankey", types_chart.Type.NORMAL, ["scratch", "headbutt"], {"HP": 40, "Attack": 80, "Defense": 35, "Speed": 70}, 3)


class Starter(enum.Enum):
    CHARMANDER = 1
    SQUIRTLE = 2
    BULBASAUR = 3
    PIKACHU = 4
    EEVEE = 5


# I dont have experience points yet so a pokemon just gains a whole level every
# time it knocks something out. the stats go up on both dicts so that leveling up
# in the middle of a battle doesnt heal you back to full
def level_up(a_pokemon):
    a_pokemon.level = a_pokemon.level + 1
    a_pokemon.base_stats["HP"] = a_pokemon.base_stats["HP"] + 4
    a_pokemon.base_stats["Attack"] = a_pokemon.base_stats["Attack"] + 3
    a_pokemon.base_stats["Defense"] = a_pokemon.base_stats["Defense"] + 3
    a_pokemon.base_stats["Speed"] = a_pokemon.base_stats["Speed"] + 3
    a_pokemon.current_stats["HP"] = a_pokemon.current_stats["HP"] + 4
    a_pokemon.current_stats["Attack"] = a_pokemon.current_stats["Attack"] + 3
    a_pokemon.current_stats["Defense"] = a_pokemon.current_stats["Defense"] + 3
    a_pokemon.current_stats["Speed"] = a_pokemon.current_stats["Speed"] + 3


def set_level(a_pokemon, wanted_level):
    while a_pokemon.level < wanted_level:
        level_up(a_pokemon)
    return a_pokemon


def full_heal(a_pokemon):
    a_pokemon.current_stats = a_pokemon.base_stats.copy()
    a_pokemon.fainted = False
