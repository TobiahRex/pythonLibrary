#!/usr/bin/env python3
from time import ctime

def times(t = []):
    t.append(ctime())
    print('t: ', t);

def addSpam(food = None):
    if food is None:
        food = []

    food.append('spam');
    print(food);

if __name__ == '__main__':
    times();
