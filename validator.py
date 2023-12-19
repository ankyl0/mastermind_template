from re import search

def sheet_validator(user_input, target_number):
    result_sheet : list = []
    if len(user_input) == 4 and search('[a-zA-Z]', user_input) == None:     # Checks that the entered number is valid.
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