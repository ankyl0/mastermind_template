from main import *
from msvcrt import getch
from os import system

def menu(ui_options, functions):
    index : int = 0
    system('cls')

    print('{:^20}'.format(f'[Welcome to Mastermind!]'))
    for i in range(len(ui_options)):
        if i == index:
            print('{:^25}'.format(f'=> {ui_options[i]} <='))
        else:
            print('{:^25}'.format(f'{ui_options[i]}'))
    while True:
        user_input = getch()
        system('cls')
        if user_input == b'w' and index != 0:
            index -=1
        elif user_input == b's' and index != len(ui_options)-1:
            index +=1
        elif user_input == b'e':
            if functions[index] != exit:
                functions[index]()
            else:
                return False
        print('{:^25}'.format(f'[Welcome to Mastermind!]'))
        for i in range(len(ui_options)):
            if index == i:
                print('{:^25}'.format(f'=> {ui_options[i]} <='))
            else:
                print('{:^25}'.format(f'{ui_options[i]}'))

def help_menu():
    pass
