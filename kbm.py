import random
import os
from nltk.corpus import words
import time
import msvcrt
import pickle


class CharacterRunner():
    def __init__(self):
        # These character sets represent specific areas a user can train
        # on the keyboard.
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
        # Attempts to load the list of users. if one does not exist, an
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

    def save_data(self, user_name):
        '''
        save_data takes the updated variable, "self.character_data", and saves
        it do a file. user_name will be the path that the data is saved to
        in the save folder.
        '''
        file_path = (r'C:\Users\MaxSteele\Documents\py_programs'
                     r'\keyboard-project\user-saves')
        with open(file_path + '\\' + user_name, 'wb') as f:
            pickle.dump(self.character_data, f)

    def update_stats(self, character, char_time, status):
        if status == 'correct':
            self.combo += 1
            self.character_data[character]['correct'] += 1
            self.answer_status = 'Correct!'
        else:
            self.combo = 0
            self.character_data[character]['incorrect'] += 1
            self.answer_status = 'incorrect!'

        self.character_data[character]['total time'] += char_time
        self.character_data[character]['average time'] = (
            self.character_data[character]['total time']
            / (self.character_data[character]['correct']
               + self.character_data[character]['incorrect']))

    def run_game(self, game_choice):
        '''
        This uses the predefined character sets to generate the character the
        user must type in correctly. Combo is updated if correct or incorrect.
        game_choice is the character set that is entered, which decides what
        type of letters, numbers, or symbols that the user must select when
        they play.
        '''
        char_time = ''

        while self.user_selection != 'Q':
            # Below will fill the list. Numbers with a weaker letters will be
            # more common so the user can get some practice.
            play_set = []
            for characters in game_choice:
                try:
                    weight = (self.character_data[characters]['correct']
                              / self.character_data[characters]['incorrect'])
                    weight = round(weight) + 1
                except ZeroDivisionError:
                    weight = 1
                for number in range(weight):
                    play_set.append(characters)
            character = play_set[random.randint(0, len(play_set) - 1)]

            os.system('cls')
            print('Enter "Q" to go to mainscreen.')
            print(f'Current Streak: {self.combo}!\n')
            if type(char_time) != str:
                print(f'Input time: {char_time:0.4f}')
            print(self.answer_status)
            print(f'Type: {character} ')
            # below is a test to view the variables.
            print('\n\n')
            print(play_set)
            print(self.character_data)

            # This section gets the input time If len of character is only 1,
            # then msvcrt is used so that return does not need to be entered.
            start_time = time.perf_counter()
            self.user_selection = msvcrt.getch().decode('utf-8')
            end_time = time.perf_counter()
            char_time = end_time - start_time

            if self.user_selection == 'Q':
                print('bye!')
                pass

            elif self.user_selection == character:
                self.update_stats(character, char_time, 'correct')

            else:
                self.update_stats(character, char_time, 'incorrect')

        # This creates a user file (if one does not exist) and pickle dumps
        # the contents into a file. This saves the accuracy for the player.
        self.save_data(self.user)

    def word_runner(self):
        '''
        Generates a word that the user needs to input correctly.
        '''
        self.combo = 0
        char_time = ''
        self.user_selection = ''

        while self.user_selection != '!':
            os.system('cls')
            word = self.word_list[random.randint(0, len(self.word_list) - 1)]
            print('Enter "!" to go to mainscreen.')
            print(f'Current Streak: {self.combo}!\n')
            print(self.answer_status)
            if type(char_time) != str:
                print(f'Input time: {char_time:0.4f}')
            print(f'Type this word: {word}.')

            start_time = time.perf_counter()
            self.user_selection = input('Enter the word: ')
            end_time = time.perf_counter()
            char_time = end_time - start_time

            if self.user_selection == '!':
                print('bye')
                break

            if self.user_selection == word:
                self.answer_status = 'Correct'
                self.combo += 1
            else:
                self.answer_status = 'Incorrect'
                self.combo = 0

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
        self.rando_string = ''
        # Creates a string of 10 random characters.
        for number in range(10):
            self.rando_string += (
                self.all_var[random.randint(0, len(self.all_var) - 1)])

        while progress != len(self.rando_string):
            # Game quits once the user has correctly input the entire string.
            if progress < 0:
                progress = 0
            os.system('cls')
            print('Type "ENDGAME" to go to mainscreen.')
            print(f'Input time: {char_time:0.4f}.')
            print(f'The b.a.s. is: {self.rando_string} ')
            print(f'Current string: {self.rando_string[:progress + 1]}' +
                  '\n')
            start_time = time.perf_counter()
            user_input = input('Enter your character: ')
            end_time = time.perf_counter()
            char_time = end_time - start_time
            if user_input == self.rando_string[:progress + 1]:
                # This checks to see if what the user entered is equal to
                # the string slice they have to enter.
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
            self.save_data(self.user)

        os.system('cls')
        print(f'Hello, {self.user}! What do you want to train?\n')
        print("1.)Numbers\n2.)Letters\n3.)Symbols\n4.)Keypad\n5.)For words."
              "\n6.)Build-a-String\ns.) To view stats.")
        print('Press "Q" to quit.')

        game_type = ''
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
            self.word_runner()
        elif game_type == '6':
            self.build_a_string()
        elif game_type == 's':
            self.show_stats()
        elif game_type == 'Q':
            print('End')

    def show_stats(self):
        # might be able to have one method to show stats. input determines
        # the type of stats that you get back.
        for char in self.character_data:
            print(
                f'{char}: Correct:{self.character_data[char]["correct"]}.'
                f'Incorrect: {self.character_data[char]["incorrect"]}.'
                f' Average time: '
                f'{self.character_data[char]["average time"]:0.2f}'
                 )

    def slowest(self):
        '''
        This prints out the characters that have the slowest input times.
        '''
        slow_list = []
        for key, value in self.character_data.items():
            slow_list.append((value['average time'], key))
        slow_list.sort(reverse=True)
        slow_list = slow_list[0:5]
        count = 1
        for item in slow_list:
            print(f'{count} | Character: {item[1]}. '
                  f'Average Speed: {item[0]:0.2f}.')
            count += 1

    def weakest(self):
        '''
        This prints out the top 5 characters with the highest error times.
        '''
        weak_list = []
        for key, value in self.character_data.items():
            try:
                # This creates a tuple with the order of:
                # (incorrect, letter, ratio, correct).
                weak_list.append((value['incorrect'],
                                  key,
                                  value['correct'] / value['incorrect'],
                                  value['correct']))
            except ZeroDivisionError:
                weak_list.append((value['incorrect'],
                                  key,
                                  value['correct'],
                                  value['correct']))
        weak_list.sort(reverse=True)
        weak_list = weak_list[0:5]
        for data in weak_list:
            print(f'Character: {data[1]}. Incorrect: {data[0]}. '
                  f'Ratio: {data[2]:0.2f}. Correct: {data[3]}.')


def start_game():
    start = CharacterRunner()
    start.mainscreen()
