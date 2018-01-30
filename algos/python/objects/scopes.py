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

def enclosedScope_outter():
    y = 'This is local scope of "enclosedScope_outter" BUT, the enclosed scope of "enclosedScope_inner"'

    def enclosedScope_inner():
        z = 'This is the local scope of "enclosedScope_inner"'.'
