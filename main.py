from game_manager import game_manager
from validations import choose_checker
from show_history import show_history
from show_statistics import show_statistics

def print_menu():
    print(f"""
    ================================
              ROLL DICE
    ================================

1. Start New Game
2. View Game History
3. View Statistics
4. Exit

Choose an option:
""")
    choose = input()
    while not choose_checker(choose):
        choose = input("only a nuber from the menu")
    choose = int(choose)
    return choose

def active1():
    print(game_manager())
def active2():
    history = show_history()
    for game in history:
        print(f"Game result:\n{game}")
def active3():
    print(show_statistics())

def main_menu():
    choice = print_menu()
    while choice != 4:
        if choice == 1:
            active1()
        elif choice == 2:
            active2()
        elif choice == 3:
            active3()
        else:
            return "Something went wrong"
        choice = print_menu()
    return "Progress has finished successfully"

print(main_menu())
