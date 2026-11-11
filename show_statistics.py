from json_manager import get_json

def show_statistics():
    statistics = {}
    sum_games = 0
    sum_player_wins = 0
    sum_computer_wins = 0
    sum_ties = 0
    player_winning_percentage = 0
    loads = get_json()
    if not loads:
        return "No games available"
    for game in loads:
        sum_games += 1
        if game["winner"] == "tie":
            sum_ties += 1
        elif game["winner"] == "Computer":
            sum_computer_wins += 1
        else:
            sum_player_wins += 1

    player_winning_percentage = round((sum_player_wins / sum_games) * 100, 2)
    statistics["all_games"] = sum_games
    statistics["player_wins"] = sum_player_wins
    statistics["computer_wins"] = sum_computer_wins
    statistics["tie_games"] = sum_ties
    statistics["players_winning_percentage"] = f"{player_winning_percentage}%"
    return statistics

