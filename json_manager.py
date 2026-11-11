import json

def get_json():
    with open("game_history.json", "r") as file:
        loads = json.load(file)
    return loads

def add_to_json(dictionary):
    loads = get_json()
    loads.append(dictionary)
    with open("game_history.json", "w") as file:
        json.dump(loads, file, indent=2)
    return "Added successfully"

def update_full_json(list_of_dict):
    with open("game_history.json", "w") as file:
        json.dump(list_of_dict, file, indent=2)
    return "json has been updated"

def beginning_dict(name, rounds):
    game_dict = {}
    game_dict["Player_name"] = name
    game_dict["rounds"] = rounds
    game_dict["player_score"] = 0
    game_dict["computer_score"] = 0
    return game_dict


def make_a_dict(new_dict, result):
    new_dict["result"].append(result)



