import random
import datetime
import re

from crisscross.cell import Cell

random.seed(datetime.datetime.now())

class Board:

    @classmethod
    def find_word(self, length, word_structure=None, word_file='files/words.txt'):
        """Return a word of length matching the word structure of word_structure from
        the word file word_file if a word can be found"""
        return_word = None
        possible_words = []
        with open(word_file) as f:
            words = (x for x in f.readlines() if x.strip().isalpha() and len(x.strip()) == length)
            for word in words:
                word_found = True
                for key, value in word_structure.items():
                             if word[int(key)].upper() != value.upper():
                                 word_found = False
                                 continue
                if word_found == True:
                    possible_words.append(word.strip().upper())
        return random.choice(possible_words)


    def __init__(self, number_of_rows=5, number_of_columns=5, emptySpaces=2):
        if emptySpaces / (number_of_columns * number_of_rows) > .25:
            raise Exception("Empty spaces must eqaual less than 25% of the board")
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.emptySpaces = emptySpaces
        self.board = [[Cell(is_blank=False) for x in range(self.number_of_columns)] for x in range(self.number_of_rows)]
        self.add_blanks_to_board()
        self.populate_board()
        
    def __str__(self):
        rendered_board = []
        for row in self.board:
            rendered_board.append(' '.join(map(str, row)) + '\n')
        return '\n' + ''.join(rendered_board)


    def add_blanks_to_board(self):
        # Pick random spaces and validate them
        for x in range(self.emptySpaces):
            made_blank_space = False
            max_tries = 1000
            while made_blank_space == False:
                max_tries -= 1
                blank_space_row = random.randint(0, self.number_of_rows-1)
                blank_space_column = random.randint(0, self.number_of_columns-1)
                if self.validate_blank_space(blank_space_row, blank_space_column):
                   made_blank_space = True
                if max_tries == 0:
                    raise Exception("Max tries exceded for blank space creation.")

    def validate_blank_space(self, empty_space_row, empty_space_column):
        """Returns true if the blank space placement doesn't
        create any one or two letter word spots in any row or
        column"""
        if self.board[empty_space_row][empty_space_column].is_blank:
            return False
        self.board[empty_space_row][empty_space_column].is_blank = True
        for row in range(self.number_of_rows):
            test_string = ''
            for column in range(self.number_of_columns):
                if self.board[row][column].is_blank:
                    test_string += '-'
                else:
                    test_string += 'X'
            matches = re.findall(r"X+", test_string)
            for x in matches:
                if len(x) < 3:
                    self.board[empty_space_row][empty_space_column].is_blank = False
                    return False
        for column in range(self.number_of_columns):
            test_string = ''
            for row in range(self.number_of_rows):
                if self.board[row][column].is_blank:
                    test_string += '-'
                else:
                    test_string += 'X'
            matches = re.findall(r"X+", test_string)
            for x in matches:
                if len(x) < 3:
                    self.board[empty_space_row][empty_space_column].is_blank = False
                    return False
        return True
                
    def populate_board(self):
        pass

    def add_horizontal_word(self, start_row, start_column, length):
        pass
    
    def add_vertical_word(self, start_row, start_column, length):