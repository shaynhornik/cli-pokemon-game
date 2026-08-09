import enum

class Pokemon:
    def __init__ (self, name, type, moves, base_stats, level):
        self.name = name
        self.type = type
        self.moves = moves
        self.base_stats = base_stats
        self.level = level
        self.current_stats = base_stats.copy()

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