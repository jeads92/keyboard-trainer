import random
import os
from nltk.corpus import words

class CharacterRunner():
    def __init__(self):
        self.numbers_var = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        self.keypad_var = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/', '*', '-', '+', '.')
        self.letter_var = ('a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l',\
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        self.symbol_var = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',\
                  '+', '=', '[', '{', ']', '}', ':', ';', "'", '|', '\\', ',',\
                      '<', '.', '>', '?', '/', '`', '~')
        self.word_list = words.words()
        self.combo = 0
        self.user_selection = ''
        self.answer_status = 'Ready Up'
        
        
    def run_game(self, game_choice):
        '''
        This used the predefined character sets to genereate the character the
        user must type in correctly. Combo is updated if correct or incorrect.
        '''
        while self.user_selection != 'ENDGAME':
            os.system('cls')
            character = game_choice[random.randint(0,len(game_choice) - 1)]
            print(f'Current Streak: {self.combo}!\n')
            print(self.answer_status)
            print(f'Number is: {character} ')
            self.user_selection = input('Type the number: ')
            if self.user_selection == 'ENDGAME':
                print('Game Ended')
            elif self.user_selection == character:
                self.combo += 1
                self.answer_status = 'Correct!'
            else:
                self.combo = 0
                self.answer_status = 'Wrong'
        
    def mainscreen(self):
        '''
        This lets the user choose which type of character set they want to
        practice.
        '''
        print('What do you want to train?')
        print('1.)Numbers\n2.)Letters\n3.)Symbols\n4.)Keypad\n5.) For words.\n')
        game_type = input('Enter game choice ')
        if game_type == '1':
            self.run_game(self.numbers_var)
        elif game_type == '2':
            self.run_game(self.letter_var)
        elif game_type == '3':
            self.run_game(self.symbol_var)
        elif game_type == '4':
            self.run_game(self.keypad_var)
        elif game_type == '5':
            self.run_game(self.word_list)
    
        
def start_game():
    start = CharacterRunner()
    start.mainscreen()