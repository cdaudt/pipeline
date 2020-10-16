# Simple example to show usage of the data processing pipes
# Parses through an array of words and prints out the ones >= 5 chars
# See https://github.com/cdaudt/pipeline for more details
# Author: Christian Daudt

words = [
    'output',
    'must',
    'should',
    'not',
    'contain',
    'seven',
    'six',
    'words',
    'listed',
    'in',
    'total',
    'fail'
]

from sources import ArraySource
from filters import DropSmallWord, PrintWord

def main():
    pw = PrintWord(None) # Save image
    ds = DropSmallWord(pw, 5)
    a = ArraySource(ds, words)
    a.run()


if __name__ == '__main__':
    main()

