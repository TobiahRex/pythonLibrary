#!/usr/bin/env python3
from itertools import repeat

m = [ 5, 3, 8, 2]

def printBreak(title = '', quantity = 10, lineBreak = '-'):
    if len(title):
        quantity = len(title)

    [lineBreak.append(lineBreak) print(lineBreak) for _ in repeat(None, quantity)]

    if (title):
        print(lineBreak);
        print(title)
        print(lineBreak)
    else:
        print(lineBreak)
``
def updateList(k):
    k.append(1)
    print('list: ', k)
    print('original list: ', m)


def updateList2(a):
    a = m
    a.append(1)
    print('list2: ', a)
    print('original list: ', m)

if __name__ == '__main__':
    updateList(m)
    printBreak()
    updateList2(m)
