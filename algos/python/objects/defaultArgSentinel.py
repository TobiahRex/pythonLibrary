#!/usr/bin/env python3
from time import ctime

def times(t = []):
    t.append(ctime())
    print('t: ', t);

def addSpam(food = None):
    if food is None:
        food = []

    return food.append('spam');

if __name__ == '__main__':
    times();
