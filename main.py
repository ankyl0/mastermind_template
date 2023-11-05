from msvcrt import getch
from os import system
from re import search
from random import randint, choice

def menu():
    index : int = 0
    ui_options : list = ['PLAYER VS PC', 'PC VS PLAYER', 'GAME RULES', 'EXIT']
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
            return index
        print('{:^25}'.format(f'[Welcome to Mastermind!]'))
        for i in range(len(ui_options)):
            if index == i:
                print('{:^25}'.format(f'=> {ui_options[i]} <='))
            else:
                print('{:^25}'.format(f'{ui_options[i]}'))

def generate_guess(previous_guesses):
    start_numbers = [0,1,2,3,4,5,6,7,8,9]
    guess_list = []
    guess : str = ''
    #Generates a number with ONLY unique characters.
    while len(guess_list) != 4:
        try:
            guess_list.append(start_numbers.pop(randint(0,9)))
        except IndexError:
            continue
    for i in range(4):
        guess += str(guess_list[i])

    return guess

def gameloop(gamemode):
    if gamemode == 0:
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
                    else:
                        guess_sheet.append('F')
                print('{:^50}'.format(f'[Round {round} Result]: ', end=''))
                print('{:^50}'.format(' '.join(guess_sheet),''), end='\n\n')
                round +=1
            else:
                print('{:^50}'.format('[INVALID INPUT, ENTER A 4 DIGIT NUMBER!]'))
        if round <=12:
            print('{:^50}'.format(f'\n[GG, The number was {user_input}, You won in {round} round(s)!]'))
            print('{:^50}'.format('[Press any key to return to menu...]'),end='')
            input()
        else:
            print('{:^50}'.format(f'[Game Over, The number was {user_input}...]'))
            print('{:^50}'.format('[Press any key to return to menu...]'),end='')
            input()

    elif gamemode == 1:
        round : int = 1
        pc_guess : str = None
        previous_guesses : list = []
        guess_sheet : str = ''

        print('{:>32}'.format('[Enter your number]: '),end='')
        player_choice = str(input())
        while pc_guess != player_choice and round != 13:
            pc_guess = generate_guess(previous_guesses)
            print('{:^32}'.format(f'[PC Guessed {pc_guess}, enter R or F]: '),end='')
            guess_sheet = [i for i in input()]

            #Runs if the pc's guess isn't correct.
            if guess_sheet != ['R', 'R', 'R', 'R']:
                previous_guesses.append(pc_guess)
            
            print(previous_guesses)


if __name__ == '__main__':
    while True:
        gamemode = menu()
        if gamemode <=1:   #Plays the game unless user has selected "Exit" (exit = 2)
            gameloop(gamemode)
        elif gamemode == 2:
            print('idk, guess or sum')
            input()
        else:
            print('[Exiting...]')
            break