# Angelica Rota SM3201142

from expressions import *
 
class Subroutine(BinaryOp):
    '''
    It does not evaluate the expression but associetes it with the variable f

    Methods:
        __init__: subroutine name and expression
        evaluate: does not evaluate the expression but associetes it with the indicated variable
        __str__ : string representation of subroutine
    '''
    def __init__(self, args):
        super().__init__(args)
        self.f = args[1].name
        self.expr = args[0]
    
    def evaluate(self, env):
        env[self.f] = self.expr
    
    def __str__(self):
        return f"defsub {self.f} {self.expr}"

class Call(UnaryOp):
    '''
    Evaluate the expression associated with the indicated variable (defined via defsub)

    Methods:
        __init__: variable name
        evaluate: evaluates the expression
        __str__ : string representation of call
    '''
    def __init__(self, args):
        super().__init__(args)
        self.f = args[0].name
    
    def evaluate(self, env):
        return env[self.f].evaluate(env)

    def __str__(self):
        return f"call {self.f}"