from urllib.request import urlopen

def fetch():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = [];
        for line in story:
            line_words = line.decode('utf-8').split();
            for word in line_words:
                story_words.append(word);

        print(' '.join(story_words))
'''
    *In a python REPL type...

    >>> import fetchPrintUrl
    >>> fetchPrintUrl.fetch()

    *Result will be the content of the request response in concatenated format.
'''

if __name__ == '__main__':
    fetch()
