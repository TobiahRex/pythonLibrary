#!/usr/bin/env Python3
'''Fetch and print text from a url.

Usage:
    python3 printWords.py <URL>
'''
import sys
from urllib.request import urlopen

def fetch(url):                                 #'http://sixty-north.com/c/t.txt'
    '''Fetch text document from <URL>

    Args:
        url: The URL of a UTF-8 text document.

    Return:
        The fetch response as a list of words.
    '''
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split();
            for word in line_words:
                story_words.append(word);
        return story_words


def print_words(words):
    '''Print list of words as a single spaced, single line string.

    Args:
        words: The list of word items to print.
    '''
    print(' '.join(words))


def main(url):
    '''Invoked directly as a script; Makes a composite call to fetch() and passes result to print().

    Args:
        url: The URL of a UTF-8 text document.
    '''
    words = fetch(url)
    print_words(words)


if __name__ == '__main__':
    url = sys.argv[1] # The 0th arg is the module filename.
    main(url)
