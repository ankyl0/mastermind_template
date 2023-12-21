from os import system
from random import randint
from re import search

ENTER_PROMPT = '[Press Enter to continue...]'

def sheet_validator(user_input, target_number):
    result_sheet : list = []
    for i in range(4):  # Loops through the user input.
        if user_input[i] == target_number[i]:   # Current index is correct.
            result_sheet.append('R')  
        elif user_input[i] in target_number:    # Checks if number exists but in wrong position.
            if len(result_sheet) != 0:
                for second_i in range(len(result_sheet)):   # Loops through the current result sheet.
                    if user_input[second_i] == user_input[i] and result_sheet[second_i] == 'X':     # If a number has been marked as X earlier, it will be marked as F instead.
                        result_sheet.append('F')
                        break
                    elif second_i == len(result_sheet)-1:   # Marks number as correct, but in wrong position.
                        result_sheet.append('X')
            else:
                result_sheet.append('X')
        else:   # Number is not in the target number.
            result_sheet.append('F')

    return result_sheet

# FIX PRINT STATEMENTS SO THEYT LOOK NICE PLEASE AND THANK YOU 
def player_vs_pc():
    # Declaring variables.
    target_number : str = str(randint(1000,9999))
    user_input : str = None
    result_sheet : list = []
    round : int = 1

    print(f'[Gamemode - Player vs AI]')
    # Gameloop.
    while target_number != user_input and round != 13:
        result_sheet = []   # Clears result sheet for new round.
        print('\n[Enter your guess]: ', end='')
        user_input = str(input())

        if len(user_input) == 4 and search('[a-zA-Z]', user_input) == None:     # Checks that the entered number is valid.
            result_sheet = sheet_validator(user_input, target_number)
            print(f'[Round {round} results: {result_sheet}]')
            round += 1
        else:
            print('[INVALID INPUT]')
        
    
    # Gameloop broken.
    if round <= 12:
        print(f'\n[GG! You won in {round} rounds!]')
        input(ENTER_PROMPT)
    else:
        print(f'[GG... you didn\'t guess the number in 12 rounds.]')
        input(ENTER_PROMPT)
    system('cls')