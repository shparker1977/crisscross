import pathlib
import pytest
import random
from datetime import datetime

wordsFilePath = pathlib.Path.cwd().joinpath('files','words.txt')
wordCount = 466515


with open(wordsFilePath) as fp:
    for i, line in enumerate(fp):
        if i == 1:
            assert(line == "a'\n")






