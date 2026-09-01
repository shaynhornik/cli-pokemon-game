#This module contains the pokemon types with weaknesses and resistances. for import into other modules.
import enum

class Type(enum.Enum):
    FIRE = "fire"
    WATER = "water"
    GRASS = "grass"
    ELECTRIC = "electric"
    NORMAL = "normal"

neutral = 1.0
super_effective = 2.0
not_very_effective = 0.5

CHART = {
    Type.FIRE: {
        "weaknesses": [Type.WATER],
        "resistances": [Type.GRASS]
    },
    Type.WATER: {
        "weaknesses": [Type.ELECTRIC, Type.GRASS],
        "resistances": [Type.FIRE]
    },
    Type.GRASS: {
        "weaknesses": [Type.FIRE],
        "resistances": [Type.WATER]
    },
    Type.ELECTRIC: {
        "weaknesses": [],
        "resistances": [Type.ELECTRIC]
    },
    Type.NORMAL: {
        "weaknesses": [],
        "resistances": []
    }
}

# the chart is built from the defenders point of view, so we look up the pokemon
# thats getting hit and then check if the move type is in its weakness list
def get_effectiveness(move_type, defending_type):
    if defending_type not in CHART:
        return neutral
    weaknesses = CHART[defending_type]["weaknesses"]
    resistances = CHART[defending_type]["resistances"]
    if move_type in weaknesses:
        return super_effective
    elif move_type in resistances:
        return not_very_effective
    else:
        return neutral
