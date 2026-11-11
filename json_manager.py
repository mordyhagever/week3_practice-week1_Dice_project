import json
from json import JSONDecoder


def get_json():
    try:
        with open("game_history.json", "r") as file:
            loads = json.load(file)
        return loads
    except json.JSONDecoder:
        raise IOError("Json is broken")


def add_to_json(dictionary):
    try:
        loads = get_json()
        loads.append(dictionary)
        with open("game_history.json", "w") as file:
            json.dump(loads, file, indent=2)
        return "Added successfully"
    except json.JSONDecoder:
        raise IOError("Json is broken")




def beginning_dict(name, rounds):
    game_dict = {}
    game_dict["Player_name"] = name
    game_dict["rounds"] = rounds
    game_dict["player_score"] = 0
    game_dict["computer_score"] = 0
    return game_dict


def make_a_dict(new_dict, result):
    new_dict["result"].append(result)



