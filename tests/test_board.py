import pathlib
import pytest
from crisscross.board import Board

def test_word_creation():
    words_file_path = pathlib.Path.cwd().joinpath('files','words.txt')
    test_word = Board.find_word(length=6, word_structure={'2':'A',}, word_file=words_file_path )
    assert len(test_word) == 6
    assert test_word[2] == 'A'
    test_word = Board.find_word(length = 5, word_structure={'1':'A','3':'S'}, word_file=words_file_path)
    assert len(test_word) == 5
    assert test_word[1] == 'A'
    assert test_word[3] == 'S'

def test_bad_board_creation():
    with pytest.raises(Exception):
        my_board = Board(10, 10, 26)

def test_board_creation():
    # Check that no single/double word spaces are made
    number_rows = 10
    number_columns = 10
    number_blanks = 25
    my_board = Board(number_rows, number_columns, number_blanks)
    blank_spaces = [my_board.board[y][z] for y in range(number_rows) for z in range(number_columns) if my_board.board[y][z].is_blank]
    assert len(blank_spaces) == number_blanks
    print(str(my_board))
    
                    

def test_board_population():
    # Check that all spots are filled with words
    pass


def test_board_solve():
    pass

def test_board_not_solved():
    pass