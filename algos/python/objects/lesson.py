#!/usr/bin/env python3
from itertools import repeat

m = [5, 3, 8, 2]

def updateList(k):
    k.append(1)
    print('list: \n', k)
    print('original list: \n', m)


def updateList2(a):
    a = m[:]
    a.append(1)
    print('list2: \n', a)
    print('original list: \n', m)

def printBreak(title = '', quantity = 10, lineBreak = '-'):
    border = ''

    if len(title):
        border = lineBreak * len(title)
    else:
        border = lineBreak * quantity

    if (title):
        print(border);
        print(title)
        print(border + '\n')
    else:
        print(border)

if __name__ == '__main__':
    # updateList(m)
    printBreak('yo', 50)
    updateList2(m)
