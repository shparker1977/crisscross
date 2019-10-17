import random

class Word:

    def __init__(self, length, start_row, start_column, orientation):
        self.length = length
        self.start_row = start_row
        self.start_column = start_column
        self.orientation = orientation

    @classmethod
    def find_word(cls, length, word_structure=None, word_file='files/words.txt'):
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