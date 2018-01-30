'''
    Local
    Enclosing
    Global
    Builtin

    "LEGB rule"

'''

#Local Scope e.g.
def localScope():
    x = 'This is a locally scoped variable - scoped by the function block' # Technically this line is "lexically scoped" - You can think of "lexical" scoping as the result of assignments or bindings.
    print('x: ', x)

def enclosedScope_outter():
    y = 'This is local scope of "enclosedScope_outter" BUT, the enclosed scope of "enclosedScope_inner"'
    print('y (outter) 1: ', y)  #y (outter) 1:  This is local scope of "enclosedScope_outter" BUT, the enclosed scope of "enclosedScope_inner"


    def enclosedScope_inner():
        z = 'This is the local scope of "enclosedScope_inner".'
        y = 'This is the Y re-assignment'
        print('y (inner): ', y)  #y (inner):  This is the Y re-assignment

    enclosedScope_inner()

    print('y (outter) 2:', y)  #y (outter) 2: This is local scope of "enclosedScope_outter" BUT, the enclosed scope of "enclosedScope_inner"

    '''
        The last print - "y (outter) 2" is still the original value even after assigned y in the inner function.
        This is because the assignment happened inside an "enclosed" scope...
        Therefore "y" was a completely different object referenc than the "y" in the outter function.
    '''
