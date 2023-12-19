from os import system
from random import randint
from validator import *

# FIX PRINT STATEMENTS SO THEYT LOOK NICE PLEASE AND THANK YOU 
def player_vs_pc():
    # Declaring variables.
    target_number : str = str(randint(1000,9999))
    user_input : str = None
    result_sheet : list = []
    round : int = 1

    print(target_number)
    # Gameloop.
    while target_number != user_input and round != 13:
        result_sheet = []   # Clears result sheet for new round.
        print('[Enter your guess: ]', end='')
        user_input = str(input())

        result_sheet = sheet_validator(user_input, target_number)
        print(result_sheet)
        round += 1
    
    # Gameloop broken.
    if round <= 12:
        print('You won!')
    else:
        print('You lost (exceeded 12 rounds.)')
    system('cls')
                