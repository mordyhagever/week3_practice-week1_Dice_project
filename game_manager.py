from unittest import result
result_dict = {}

from validations import *
from roll_dice import random_dicing
from json_manager import *

def get_name():
    name = input("Enter your name: ")
    while not check_name(name):
        name = input("Enter a non empty name: ")
    return name

def get_rounds():
    rounds = input("Enter a number of rounds between 1-10: ")
    while not check_rounds(rounds):
        rounds = input("rounds only between 1-10: ")
    rounds = int(rounds)
    return rounds


def add_turn(name):
   dice1 = random_dicing()
   dice2 = random_dicing()
   print(f"{name}'s dice: {dice1}")
   print(f"computer dice: {dice2}")
   return dice1, dice2


def game_manager():
    winner = None
    name = get_name()
    player_counter = 0
    computer_counter = 0
    rounds = get_rounds()
    game_dict = beginning_dict(name, rounds)
    global result_dict
    game_dict["result"] = []
    for i in range(rounds):
        result = {}
        round_win = None
        print(f"-------Round {i + 1} --------")
        dices = add_turn(name)
        player_counter += dices[0]
        computer_counter += dices[1]
        result["round"] = i + 1
        result["player_dice"] = dices[0]
        result["computer_dice"] = dices[1]
        if dices[0] > dices[1]:
            round_win = name
        elif dices[1] > dices[0]:
            round_win = "Computer"
        else:
            round_win = "tie"
        result["winner"] = round_win
        result_dict = make_a_dict(game_dict, result)
    if player_counter > computer_counter:
        winner = name
    elif computer_counter > player_counter:
        winner = "Computer"
    else:
        winner = "tie"

    result_dict["player_score"] = player_counter
    result_dict["computer_score"] = computer_counter
    print(f"""
    ====================
         GAME OVER
    ====================
    The winner is: {winner.upper()}!!!
""")
    add_to_json(result_dict)
    return "Game had added successfully"


print(game_manager())
