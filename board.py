import random
import datetime
import re

from crisscross.cell import Cell
from criscross.word import Word

random.seed(datetime.datetime.now())

class Board:

    def __init__(self, number_of_rows=5, number_of_columns=5, emptySpaces=2):
        if emptySpaces / (number_of_columns * number_of_rows) > .25:
            raise Exception("Empty spaces must eqaual less than 25% of the board")
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.emptySpaces = emptySpaces
        self.board = [[Cell(is_blank=False) for x in range(self.number_of_columns)] for x in range(self.number_of_rows)]
        self.word_map = {}
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
            max_tries = 100
            while made_blank_space == False:
                max_tries -= 1
                blank_space_row = random.randint(0, self.number_of_rows-1)
                blank_space_column = random.randint(0, self.number_of_columns-1)
                if self.validate_blank_space(blank_space_row, blank_space_column):
                   self.board[blank_space_row][blank_space_column].value = '-' 
                   made_blank_space = True
                if max_tries == 0:
                    self.board = [[Cell(is_blank=False) for x in range(self.number_of_columns)] for x in range(self.number_of_rows)]
                    return self.add_blanks_to_board()

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
        self.get_word_map()
        while not self.board_populated() and self.word_map != {}:
            self.populate_words(max(self.word_map.keys()))
            self.word_map.pop(max(self.word_map.keys()))

          
    def get_word_map(self):
        # Find horizontal words
        for row in range(self.number_of_rows):
            mapped_row = list(map(str, self.board[row]))
            if '-' not in mapped_row:
                if self.number_of_rows not in self.word_map.keys():
                    self.word_map[self.number_of_rows] = []
                self.word_map[self.number_of_rows].append((row, 0, 'horizontal'))
            else:
                start_pos = 0
                blank_count = mapped_row.count('-')
                for x in range(blank_count):
                    if mapped_row.index('-') not in self.word_map.keys():
                        self.word_map[mapped_row.index('-')] = []
                    self.word_map[mapped_row.index('-', start_pos)].append((row, start_pos, 'horizontal'))
                    start_pos = mapped_row.index('-')
        # Find vertical words
        for column in range(self.number_of_columns):
            transposed_column = [self.board[x][column] for x in self.number_of_rows]
            mapped_column = list(map(str, transposed_column))
            


    def board_populated(self):
        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                if self.board[row][column].is_blank == False and \
                self.board[row][column].value == ' ':
                    return False
        return True

    def populate_words(self, key):
        """Process all of the words of length key"""
        for word in self.word_map[key]:
            if word[2] == 'horizontal':
                word_profile = self.board[word[0]][word[1]:word[1] + key]
            if word[2] == 'vertical'

