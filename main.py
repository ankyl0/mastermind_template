from player_vs_pc import *
from ai_vs_player import *
from msvcrt import getch
from os import system

def menu(title, options_list, functions_list):
    index : int = 0
    system('cls')
    print(f'{title : ^32}\n')
    for i in range(len(options_list)):
        if i == index:
            print(f"{'=>': <3}{options_list[i] : ^25}")
        else:
            print(f"{'  ' : <3}{options_list[i] : ^25}")
    while True:
        user_input = getch()
        system('cls')
        if user_input == b'w' and index != 0:
            index -=1
        elif user_input == b's' and index != len(options_list)-1:
            index +=1
        elif user_input == b'e':
            for i in range(len(functions_list)):
                if i == index : functions_list[i]()
        print(f'{title : ^32}\n')
        for i in range(len(options_list)):
            if index == i:
                print(f"{'=>': <3}{options_list[i] : ^25}")
            else:
                print(f"{'  ' : <3}{options_list[i] : ^25}")
                
def main():
    index = menu('HELLO', ['PLAYER VS PC', 'PC VS PLAYER', 'HELP', 'EXIT'], [player_vs_pc, ai_vs_player])

def main():
    selection = True
    while selection == True:
        selection = menu(['PLAYER VS PC', 'PC VS PLAYER', 'HELP', 'EXIT'], [player_vs_pc, pc_vs_player, help_menu, exit])
    print('[Exiting...]')
if __name__ == '__main__':
    main()
