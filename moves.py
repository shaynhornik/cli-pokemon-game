#This module contains a dict of moves and functions related to moves.
import types_chart

MOVES = {
    "scratch": {
        "type": types_chart.Type.NORMAL,
        "power": 40,
        "accuracy": 100
    },
    "tackle": {
        "type": types_chart.Type.NORMAL,
        "power": 40,
        "accuracy": 100
    },
    "ember": {
        "type": types_chart.Type.FIRE,
        "power": 40,
        "accuracy": 100
    },
    "water gun": {
        "type": types_chart.Type.WATER,
        "power": 40,
        "accuracy": 100
    },
    "vine whip": {
        "type": types_chart.Type.GRASS,
        "power": 45,
        "accuracy": 100
    },
    "thunder shock": {
        "type": types_chart.Type.ELECTRIC,
        "power": 40,
        "accuracy": 100
    },
    "quick attack": {
        "type": types_chart.Type.NORMAL,
        "power": 40,
        "accuracy": 100
    },
    "gust": {
        "type": types_chart.Type.NORMAL,
        "power": 40,
        "accuracy": 100
    },
    "headbutt": {
        "type": types_chart.Type.NORMAL,
        "power": 70,
        "accuracy": 90
    },
    "absorb": {
        "type": types_chart.Type.GRASS,
        "power": 20,
        "accuracy": 100
    },
    "razor leaf": {
        "type": types_chart.Type.GRASS,
        "power": 55,
        "accuracy": 95
    },
    "bubble": {
        "type": types_chart.Type.WATER,
        "power": 40,
        "accuracy": 100
    },
    "spark": {
        "type": types_chart.Type.ELECTRIC,
        "power": 65,
        "accuracy": 100
    },
    "flame wheel": {
        "type": types_chart.Type.FIRE,
        "power": 60,
        "accuracy": 100
    },
}


def get_move(move_name):
    if move_name in MOVES:
        return MOVES[move_name]
    else:
        #if I ever typo a move name in the pokemon module I want to know about it
        print(f"Error: the move '{move_name}' is not in the MOVES dict.")
        return None
