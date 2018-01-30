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

def outter():
    y = 'This is local scope of "enclosedScope_outter" BUT, the enclosed scope of "inner"'
    print('y (outter) 1: ', y)  #y (outter) 1:  This is local scope of "enclosedScope_outter" BUT, the enclosed scope of "inner"


    def inner():
        z = 'This is the local scope of "inner".'
        y = 'This is the Y re-assignment'
        print('y (inner): ', y)  #y (inner):  This is the Y re-assignment

    inner()

    print('y (outter) 2:', y)  #y (outter) 2: This is local scope of "enclosedScope_outter" BUT, the enclosed scope of "inner"

    '''
        The last print - "y (outter) 2" is still the original value even after assigned y in the "inner" function.
        This is because the assignment happened inside an "enclosed" scope...
        Therefore "y" was a completely different object reference than the "y" in the "outter" function.
    '''

globalVar = 3

def redefine():
    globalVar = 5

# redefine()
# print(globalVar) # 3
'''
    The redefinition of "globalVar" inside "redefine" does not change the global variable "globalVar" in the module scope.
    Instead, a NEW "globalVar" object reference is created within the Local Scope of the "redefine()" function.

    To re-assign the global variable "globalVar" from within a locally scoped function, the following must be done...
'''

def show():
    print(globalVar)

def redefine2():
    global globalVar
    globalVar = 5
