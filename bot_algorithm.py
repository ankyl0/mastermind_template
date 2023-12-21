from main import *

def generate_guess(previous_guesses, previous_results):   #The algorithm the computer uses to generate a new guess every round, only runs when its PC vs Player.
    start_numbers = [0,1,2,3,4,5,6,7,8,9]
    initial_guess = []

    final_guess = []
    correct_numbers = []
    banned_numbers = []
    guess : str = ''
    #Generates a number with ONLY unique characters.
    if len(previous_guesses) == 0:
        while len(initial_guess) != 4:
            try:
                initial_guess.append(start_numbers.pop(randint(0,9)))
            except IndexError:
                continue
        for i in range(4):
            guess += str(initial_guess[i])
    else:
        while True:
            guess = int(previous_guesses[len(previous_guesses)-1])
            prev_result = previous_guesses[len(previous_results)-1]
            for index in range(0,len(prev_result)):
                if prev_result[index] == 'R':
                    final_guess.append(guess[index])
                elif prev_result[index] == 'X':
                    correct_numbers.append(guess[index])
            break

    return guess