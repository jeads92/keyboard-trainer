import random
import os
from nltk.corpus import words
import time
import msvcrt
import pickle


class CharacterRunner():
    def __init__(self):
        self.numbers_var = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        self.keypad_var = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                           '/', '*', '-', '+', '.')
        self.letter_var = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                           'u', 'v', 'w', 'x', 'y', 'z')
        self.symbol_var = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                           '-', '_', '+', '=', '[', '{', ']', '}', ':', ';',
                           "'", '|', '\\', ',', '<', '.', '>', '?', '/', '`',
                           '~')
        self.word_list = words.words()
        self.all_var = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/',
                        '*', '-', '+', '.', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                        'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#',
                        '$', '%', '^', '&', '(', ')', '_', '=', '[', '{', ']',
                        '}', ':', ';', "'", '|', '\\', ',', '<', '.', '>',
                        '?', '`', '~')
        self.combo = 0
        self.user_selection = ''
        self.answer_status = 'Ready Up'
        self.rando_string = ''
        self.user = ''
        self.character_data = {}
        # Attempts to load a save data of users. if one does not exist, an
        # empty one is created
        try:
            f = open(r"C:\Users\MaxSteele\Documents\py_programs"
                     r"\keyboard-project\list-of-users\user-list", 'rb')
            self.user_list = pickle.load(f)
        except FileNotFoundError:
            self.user_list = []
            f = open(r"C:\Users\MaxSteele\Documents\py_programs"
                     r"\keyboard-project\list-of-users\user-list", 'w+')
            f.close()

    def run_game(self, game_choice):
        '''
        This uses the predefined character sets to genereate the character the
        user must type in correctly. Combo is updated if correct or incorrect.
        '''
        char_time = ''
        while self.user_selection != 'Q':
            os.system('cls')
            character = game_choice[random.randint(0, len(game_choice) - 1)]
            print(f'Current Streak: {self.combo}!\n')
            if type(char_time) != str:
                print(f'Input time: {char_time:0.4f}')
            print(self.answer_status)
            print(f'Type: {character} ')

            if len(character) == 1:
                start_time = time.perf_counter()
                self.user_selection = msvcrt.getch().decode('utf-8')
                end_time = time.perf_counter()
            else:
                start_time = time.perf_counter()
                self.user_selection = input('Type the number: ')
                end_time = time.perf_counter()
            char_time = end_time - start_time
            if self.user_selection == 'Q':
                print('Game Ended')
            elif self.user_selection == character:
                if len(character) == 1:
                    self.combo += 1
                    self.character_data[character]['correct'] += 1
                    self.answer_status = 'Correct!'
                    self.character_data[character]['total time'] += char_time
                    self.character_data[character]['average time'] = (
                        self.character_data[character]['total time']
                        / (self.character_data[character]['correct']
                           + self.character_data[character]['incorrect']))
            else:
                if len(character) == 1:
                    self.combo = 0
                    self.character_data[character]['incorrect'] += 1
                    self.answer_status = 'Wrong'
                    self.character_data[character]['total time'] += char_time
        # This creates a user file and pickle dumps the contents into a file.
        with open(r"C:\Users\MaxSteele\Documents\py_programs"
                  r"\keyboard-project\user-saves" + '\\' + self.user,
                  'wb') as f:
            pickle.dump(self.character_data, f)

    def build_a_string(self):
        '''
        This builds a randomly-generated string from all characters on the
        keyboard. The user then must type the string correctly. They start at
        the character, then move on to the first and second character, and keep
        on moving up until they correctly type the full string.
        '''
        progress = 0
        user_input = ''
        char_time = 0
        for number in range(10):
            self.rando_string += (
                self.all_var[random.randint(0, len(self.all_var) - 1)])
        while progress != len(self.rando_string):
            if progress < 0:
                progress = 0
            os.system('cls')
            print(f'Input time: {char_time:0.4f}.')
            print(f'The b.a.s. is {self.rando_string}.')
            print(f'Current string: {self.rando_string[:progress + 1]}' +
                  '\n')
            start_time = time.perf_counter()
            user_input = input('Enter your character: ')
            end_time = time.perf_counter()
            char_time = end_time - start_time
            if user_input == self.rando_string[:progress + 1]:
                progress += 1
            elif user_input == 'ENDGAME':
                print('bye')
                break
            else:
                progress -= 1

    def mainscreen(self):
        '''
        This lets the user log into or create a profile. It also lets them
        choose which type of character set they want to practice.
        '''
        print(f'Current users: {self.user_list}.')
        self.user = input('Enter your name!\n ')
        if self.user in self.user_list:
            with open(r"C:\Users\MaxSteele\Documents\py_programs"
                      r"\keyboard-project\user-saves" + '\\' + self.user,
                      'rb') as f:
                self.character_data = pickle.load(f)
        else:
            # initialized character data for a new user. All correct and
            # incorrect ticks are set to 0.
            self.user_list.append(self.user)
            # Update the Save file for the list of users
            with open(r"C:\Users\MaxSteele\Documents\py_programs"
                      r"\keyboard-project\list-of-users\user-list", 'wb') as f:
                pickle.dump(self.user_list, f)
            for item in self.all_var:
                self.character_data[item] = {'correct': 0,
                                             'incorrect': 0,
                                             'total time': 0,
                                             'average time': 0}
            # This dumps the user data into their file.
            with open(r"C:\Users\MaxSteele\Documents\py_programs"
                      r"\keyboard-project\user-saves" + '\\' + self.user,
                      'wb') as f:
                pickle.dump(self.character_data, f)
        print('What do you want to train?')
        print(('1.)Numbers\n2.)Letters\n3.)Symbols\n4.)Keypad\n5.)For words.\
               \n6.)Build-a-String'))

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
        elif game_type == '6':
            self.build_a_string()


def start_game():
    start = CharacterRunner()
    start.mainscreen()
