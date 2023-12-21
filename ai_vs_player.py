from random import randint
from itertools import permutations
from os import system

ENTER_PROMPT = '[Press Enter to continue...]'

def generate_code():
    guess = []
    numbers = [1,2,3,4,5,6,7,8,9]
    while len(guess) != 4:
            try:
                guess.append(numbers.pop(randint(0,9)))
            except IndexError:
                continue
    return guess  # Gives code with only unique numbers.

def evaluate_guess(secret_code, guess):
    exact_matches = sum(s == g for s, g in zip(secret_code, guess))    # Number of exact matches
    partial_matches = sum(min(secret_code.count(digit), guess.count(digit)) for digit in set(secret_code)) - exact_matches

    return exact_matches, partial_matches

def make_advanced_guess(previous_guesses, previous_feedbacks):
    if not previous_guesses or not previous_feedbacks:
        return generate_code()  # If no previous feedback, make a random guess

    all_possible_codes = list(permutations(range(10), 4))
    filtered_codes = []

    # Filter possible codes based on previous feedback
    for code in all_possible_codes:
        valid = True
        for prev_guess, prev_feedback in zip(previous_guesses, previous_feedbacks):
            exact_matches, partial_matches = evaluate_guess(list(code), prev_guess)
            if (exact_matches, partial_matches) != prev_feedback:
                valid = False
                break
        if valid:
            filtered_codes.append(list(code))

    # Choose the code that maximizes information gain
    best_guess = None
    best_info_gain = -1

    # Loops through all filtered codes.
    for code in filtered_codes:
        info_gain = calculate_information_gain(code, filtered_codes)
        if info_gain >= best_info_gain:
            best_guess = code
            best_info_gain = info_gain

    if best_guess != None:  # Ensures program doesn't return None (will crash otherwise :()      
        return best_guess
    else:
        return generate_code()

def calculate_information_gain(code, possible_codes):
    # Calculates how much information given by each code.
    info_gain = 0
    for possible_code in possible_codes:
        _, _ = evaluate_guess(code, possible_code)
        info_gain += 1
    return info_gain
        
def ai_vs_player():
    # Declaring variables.
    code = [int(digit) for digit in input("Enter the secret code (4 digits): ")]
    round = 0
    previous_guesses = []
    previous_feedbacks = []
    guess = []
    
    while guess != code and round != 13:
        guess = make_advanced_guess(previous_guesses, previous_feedbacks)

        # Prints feedback.
        print(f"[Attempt {round + 1}: {guess}]")
        exact_matches, partial_matches = evaluate_guess(code, guess)
        print(f"[Results: {exact_matches} exact matches, {partial_matches} partial matches]\n")

        # Stores feedback for future reference.
        previous_guesses.append(guess)
        previous_feedbacks.append((exact_matches, partial_matches))
        round += 1

    if guess == code:
        print(f'[GG, The code was {guess}! I guessed it in {round} rounds!]')
        input()
    else:
        print('[gg, I couldn\'t guess it under 13 rounds :(]')
        input()
    system('cls')
    