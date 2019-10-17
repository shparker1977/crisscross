import pathlib
import pytest
from crisscross.board import Board

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