from crisscross.board import Board

def test_word_creation():
    test_word = Board.findWord(length=6, word_structure={'2':'A',})
    assert len(test_word) == 6
    assert test_word[2] == 'A'
    #raise Exception(test_word)
    test_word = Board.findWord(length = 5, word_structure={'1':'A','3':'S'})
    assert len(test_word) == 5
    assert test_word[1] == 'A'
    assert test_word[3] == 'S'

    
def test_board_creation():
    # Check that spaces meet specs
    # Check that no single/double word spaces are made
    # Check that 
    pass

def test board_population():
    # Check that all spots are filled with words
    pass


def test_board_solve():
    pass

def test_board_not_solved():
    pass