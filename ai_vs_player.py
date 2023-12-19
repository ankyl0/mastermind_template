from os import system
from re import search
from random import randint
from validator import *

def generate_guess(previous_guesses, correct_numbers, banned_numbers, target_number):
    ai_guess : list = []
    
    # Generates initial guess of only unique numbers.
    if len(previous_guesses) == 0:
        numbers = list(range(1,10))
        while len(ai_guess) != 4:
            index = randint(0,10)
            try:
                ai_guess.append(numbers[index])
                numbers.pop(index)
            except IndexError:
                continue
        return ai_guess
    
    else:
        previous_guess_result = sheet_validator(str(previous_guesses[len(previous_guesses)-1]), target_number)
        print(previous_guess_result)
        input()

def ai_vs_player():
    # Declaring variables.
    target_number : str = '3232'
    ai_guess : str = None
    result_sheet : list = []
    previous_guesses : list = []
    round : int = 1

    # Declaring variables used in "generate_guess" function.
    banned_numbers = []
    correct_numbers = []
    
    while ai_guess != target_number and round != 13:
        result_sheet = []
        ai_guess = generate_guess(previous_guesses, correct_numbers, banned_numbers, target_number)

        previous_guesses.append(ai_guess)
        round += 1


    
