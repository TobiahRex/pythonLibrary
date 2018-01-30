'''
    Python is a DYNAMIC & STRONG type system.

    Dynamically typed languages, are so because they are not exectuded until the program that they are defining is run.
    In contrast, languages like Java, C, C++ all run their programs BEFORE they are actually executed.  Hence their Strict type system.

    Python does NOT allow for type's to be IMPLICITLY altered when combining certain types - hence "STRONG".
    ("if" statements and "while" loop predicates are converted to "Bool" type for truthy or falsey evals).
    The requirement for this to take place is that when calling certain global/module methods with certain types,
    that type must have a defined support for that method.
'''
def add(a, b):
    result = a + b
    print(result)

result = add('tobiah', 'rex')

result = add(1.230, 1.707)

result = add([1, 3], [2, 4])

# add('Tobiah', 29)
