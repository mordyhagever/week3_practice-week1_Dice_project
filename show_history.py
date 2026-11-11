from json_manager import get_json

def show_history():
    loads = get_json()
    history_shower = []
    for game in loads:
        small_dict = {}
        small_dict["Player_name"] = game["Player_name"]
        small_dict["rounds"] = game["rounds"]
        small_dict["player_score"] = game["player_score"]
        small_dict["computer_score"] = game["computer_score"]
        small_dict["winner"] = game["winner"]
        history_shower.append(small_dict)
    if history_shower:
        return history_shower

    return "There's no games available"

