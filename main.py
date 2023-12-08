from re import search
from random import randint, choice

from bot_algorithm import *
from ui_stuff import *

def player_vs_pc():
    pc_choice : str = str(randint(1000, 9999))
    guess_sheet : list = []
    user_input : str = None
    round : int = 1
    print('{:^50}'.format(f'[Currently Playing: PLAYER VS PC]\n'))
    while pc_choice != user_input and round !=13:
        guess_sheet = []
        print('{:>32}'.format('[Enter your guess]: '),end='')
        user_input = str(input())
        if len(user_input) == 4 and search('[a-zA-Z]', user_input) == None:
            for i in range(4):
                if user_input[i] == pc_choice[i]:
                    guess_sheet.append('R')
                elif user_input[i] in pc_choice:
                    guess_sheet.append('X')
                else:
                    guess_sheet.append('F')
            print('{:^50}'.format(f'[Round {round} Result]: ', end=''))
            print('{:^50}'.format(' '.join(guess_sheet),''), end='\n\n')
            round +=1
        else:
            print('{:^50}'.format('[INVALID INPUT, ENTER A 4 DIGIT NUMBER!]'))

    # Player guessed the number within 12 rounds.
    if round <=12:
        print('{:^50}'.format(f'\n[GG, The number was {user_input}, You won in {round} round(s)!]'))
        print('{:^50}'.format('[Press any key to return to menu...]'),end='')
        input()

    # Player didn't guess the number within 12 rounds.
    else:
        print('{:^50}'.format(f'[Game Over, The number was {user_input}...]'))
        print('{:^50}'.format('[Press any key to return to menu...]'),end='')
        input()

def pc_vs_player():
    round : int = 1
    pc_guess : str = None
    previous_guesses : list = []
    previous_results : list = []
    guess_sheet : str = ''

    print('{:>32}'.format('[Enter your number]: '),end='')
    player_choice = str(input())
    while pc_guess != player_choice and round != 13:
        pc_guess = generate_guess(previous_guesses, previous_results)
        print('{:^32}'.format(f'[PC Guessed {pc_guess}, enter R or F]: '),end='')
        guess_sheet = [i for i in input()]

        #Runs if the pc's guess isn't correct.
        if guess_sheet != ['R', 'R', 'R', 'R']:
            previous_guesses.append(pc_guess)
        
        print(previous_guesses)

def main():
    selection = True
    while selection == True:
        selection = menu(['PLAYER VS PC', 'PC VS PLAYER', 'HELP', 'EXIT'], [player_vs_pc, pc_vs_player, help_menu, exit])
    print('[Exiting...]')
if __name__ == '__main__':
    main()
    