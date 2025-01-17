from player_vs_pc import *
from ai_vs_player import *
from msvcrt import getch
from os import system
ENTER_PROMPT = '[Press Enter to continue...]'

def help():
    print(f'[Commands]\n- E = Select\n- W/S = Move cursor up and down\n\n[Gamemodes]\n- Player vs PC = The player attempts to guess a number generated by the computer.\n- PC vs Player = The PC attempts to guess a number given by the user.')
    input(ENTER_PROMPT)
    system('cls')

def menu(title, options_list, functions_list):
    index : int = 0
    system('cls')
    print(f'{title}\n')
    for i in range(len(options_list)):
        if i == index:
            print(f"{'=>': <3}{options_list[i]}")
        else:
            print(f"{'  ' : <3}{options_list[i]}")
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
        print(f'{title}\n')
        for i in range(len(options_list)):
            if index == i:
                print(f"{'=>': <3}{options_list[i]}")
            else:
                print(f"{'  ' : <3}{options_list[i]}")
                
def main():
    index = menu('[Mastemind]', ['PLAYER VS PC', 'PC VS PLAYER', 'HELP', 'EXIT'], [player_vs_pc, ai_vs_player, help])

if __name__ == '__main__':
    main()
