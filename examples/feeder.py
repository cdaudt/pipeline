# Simple example to show usage of the data processing pipes
# Parses through an array of words and prints out the ones >= 5 chars
# See https://github.com/cdaudt/pipeline for more details
# Author: Christian Daudt
from sources import ArraySource
from filters import DropSmallWord, PrintWord
import procpipe

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

def main():
    print ("Procpipe version:{}".format(procpipe.__version__))
    pw = PrintWord(None) # Save image
    ds = DropSmallWord(pw, 5)
    a = ArraySource(ds, words)
    a.run()


if __name__ == '__main__':
    main()

