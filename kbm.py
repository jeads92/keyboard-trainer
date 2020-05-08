import random
import os
from nltk.corpus import words

def mainscreen():
    print('What do you want to train?')
    print('1.)Numbers\n2.)Letters\n3.)Symbols\n4.)Keypad\n5.) For words.\n')
    game_type = input('Enter game choice ')
    if game_type == '1':
        numbers_trainer()
    elif game_type == '2':
        letter_trainer()
    elif game_type == '3':
        symbol_trainer()
    elif game_type == '4':
        keypad_trainer()
    elif game_type == '5':
        word_trainer()

def numbers_trainer():
    '''Creates a tuple that houses numbers, assigns a variable that is a number
    then the user must correctly guess that number.'''
    numbers_var = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    combo = 0
    user_selection = ''
    answer_status = 'Ready up.'
    while user_selection != 'quit':
        os.system('cls')
        number_selection = numbers_var[random.randint(0,9)]
        print(f'Current Streak: {combo}!\n')
        print(answer_status)
        print(f'Number is: {number_selection} ')
        user_selection = input('Type the number: ')
        if user_selection == 'quit':
            print('Game Ended')
        elif user_selection == number_selection:
            combo += 1
            answer_status = 'Correct!'
        else:
            combo = 0
            answer_status = 'Wrong'
            
            
def keypad_trainer():
    '''uses a tuple to contain the numbers and symbols on the keypad and 
    randomly generates which character the user must input.'''
    keypad_var = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/', '*', '-', '+', '.')
    combo = 0
    user_selection = ''
    answer_status = 'Ready up.'
    while user_selection != 'quit':
        os.system('cls')
        keypad_selection = keypad_var[random.randint(0, 14)]
        print(f'Current Streak: {combo}!\n')
        print(answer_status)
        print(f'Character is: {keypad_selection} ')
        user_selection = input('Type the character: ')
        if user_selection == 'quit':
            print('Game Ended')
        elif user_selection == keypad_selection:
            combo += 1
            answer_status = 'Correct!'
        else:
            combo = 0
            answer_status = 'Wrong'
            
            
def letter_trainer():
    '''uses a tuple to store all letters. Then user used must type in the 
    letter.'''
    letter_var = ('a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l',\
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    combo = 0
    user_selection = ''
    answer_status = 'Ready up.'
    while user_selection != 'quit':
        os.system('cls')
        letter_selection = letter_var[random.randint(0, 25)]
        print(f'Current Streak: {combo}!\n')
        print(answer_status)
        print(f'Character is: {letter_selection} ')
        user_selection = input('Type the character: ')
        if user_selection == 'quit':
            print('Game Ended')
        elif user_selection == letter_selection:
            combo += 1
            answer_status = 'Correct!'
        else:
            combo = 0
            answer_status = 'Wrong'
    
    
def symbol_trainer():
    '''uses a tuple to store all symbols. Then user used must type in the 
    symbol.'''
    symbol_var = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',\
                  '+', '=', '[', '{', ']', '}', ':', ';', "'", '|', '\\', ',',\
                      '<', '.', '>', '?', '/', '`', '~')
    combo = 0
    user_selection = ''
    answer_status = 'Ready up.'
    while user_selection != 'quit':
        os.system('cls')
        symbol_selection = symbol_var[random.randint(0, int(len(symbol_var) - 1))]
        print(f'Current Streak: {combo}!\n')
        print(answer_status)
        print(f'Character is: {symbol_selection} ')
        user_selection = input('Type the character: ')
        if user_selection == 'quit':
            print('Game Ended')
        elif user_selection == symbol_selection:
            combo += 1
            answer_status = 'Correct!'
        else:
            combo = 0
            answer_status = 'Wrong'
        
def word_trainer():
    '''uses a list to store all a big list of words. Then user used must type in the 
    words.'''
    word_list = words.words()
    combo = 0
    user_selection = ''
    answer_status = 'Ready up.'
    while user_selection != 'q':
        os.system('cls')
        word_selection = word_list[random.randint(0, 236735)]
        print(f'Current Streak: {combo}!\n')
        print(answer_status)
        print(f'Word is: {word_selection} ')
        user_selection = input('Type the word: ')
        if user_selection == 'q':
            print('Game Ended')
        elif user_selection == word_selection:
            combo += 1
            answer_status = 'Correct!'
        else:
            combo = 0
            answer_status = 'Wrong'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    