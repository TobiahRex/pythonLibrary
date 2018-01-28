def match(expression): # "def" is required when defining a function
    ### This is called a 'docstring'.  It uses 3 pound signs on the outside.  You can think of it like JS's /**/ comment syntax. ###
    stack = []

    dict = {'(':')', '[':']', '{':'}'}
    for x in expression:
        if dict.get(x):
            stack.append(dict[x])
        else:
            if len(stack) == 0 or x != stack[len(stack)-1]:
                return False
            stack.pop()
    return len(stack) == 0
