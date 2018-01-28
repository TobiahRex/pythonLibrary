'''Fetch and print document text from a url.

Usage:
    python3 fetchBook.py <URL>
'''
import sys
from urllib.request import urlopen

def fetch(url):                                 #'http://sixty-north.com/c/t.txt'
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split();
            for word in line_words:
                story_words.append(word);
        return story_words


def print_items(items):
    print(' '.join(items))


def main(url):
    words = fetch(url)
    print_items(words)


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
