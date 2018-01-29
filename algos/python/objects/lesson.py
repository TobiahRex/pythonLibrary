#!/usr/bin/env python3
m = [ 5, 3, 8, 2]

def printBreak(title, lineBreak = '-'):
    for break in len(title):
        print(lineBreak);
        print(title)
        print(lineBreak)

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
    print()
    updateList2(m)
