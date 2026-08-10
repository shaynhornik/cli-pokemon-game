#This module contains the pokemon types with weaknesses and resistances. for import into other modules.
import enum

class Type(enum.Enum):
    FIRE = "fire"
    WATER = "water"
    GRASS = "grass"
    ELECTRIC = "electric"
    NORMAL = "normal"

neutral = 1.0

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