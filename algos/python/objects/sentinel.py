#!/usr/bin/env python3
from time import ctime


'''
    At module runtime, the function times() is defined, and the default argument is assigned the value [] at that moment.
    Later, each occurence of invocation appends to the same list.
    It does NOT re-defined the default argument as an empty list as may be expected.
'''
def times(t = []):
    t.append(ctime())
    print('t: ', t);


'''
    At module runtime, the function addSpam() is defined and the default argument 'food' is defined as None.
'''
def addSpam(food = None):
    if food is None:
        food = []

    food.append('spam');
    print(food);

if __name__ == '__main__':
    times();
