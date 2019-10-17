import pathlib
from crisscross.word import Word

def test_word_creation():
    words_file_path = pathlib.Path.cwd().joinpath('files','words.txt')
    test_word = Word.find_word(length=6, word_structure={'2':'A',}, word_file=words_file_path)
    assert len(test_word) == 6
    assert test_word[2] == 'A'
    test_word = Word.find_word(length = 5, word_structure={'1':'A','3':'S'}, word_file=words_file_path)
    assert len(test_word) == 5
    assert test_word[1] == 'A'
    assert test_word[3] == 'S'