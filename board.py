import random
import datetime

random.seed(datetime.datetime.now())

class Board:

    @classmethod
    def findWord(self, length, word_structure=None):
        word_found = False
        return_word = None
        possible_words = []
        with open('files/words.txt') as f:
            words = [x for x in f.readlines() if x.strip().isalpha() and len(x.strip()) == length]
            for _, v in word_structure.items():
                words = [x for x in words if v in x]
            for word in words:
                for key, value in word_structure.items():
                             if word[int(key)] == value:
                                 word_found = True
                             else:
                                 word_found = False
                                 break
                if word_found == True:
                    possible_words.append(word.strip().upper())
        return random.choice(possible_words)


    def __init__(self, numberOfRows=5, numberOfColumns=7, emptySpaces=5):
        self.numberOfRows = numberOfRows
        self.numberOfColumns = numberOfColumns
        self.emptySpaces = emptySpaces
        self.board = [['X' for x in range(self.numberOfColumns)] for x in range(self.numberOfRows)]
        self.createBlankBoard()
        
    def __str__(self):
        return "\n".join([" ".join(x) for x in self.board])

    def createBlankBoard(self):
        ## Add restrictions for where spaces can be (i.e. next to themselves)
        for x in range(self.emptySpaces):
            madeBlankSpace = False
            while madeBlankSpace == False:
                blankSpaceRow = random.randint(0, self.numberOfRows-1)
                blankSpaceColumn = random.randint(0, self.numberOfColumns-1)
                if self.board[blankSpaceRow][blankSpaceColumn] == 'X':
                    self.board[blankSpaceRow][blankSpaceColumn] = '-'
                    madeBlankSpace = True



            
