# Angelica Rota SM3201142

from expressions import *

class Print(UnaryOp):
    '''
    Evaluate expr and print the result.

    Methods:
        __init__: expression
        evaluate: returns the value of expr
        __str__ : string representation of print
    '''
    def __init__(self, args):
        super().__init__(args)
        self.expr = args[0]
    
    def evaluate(self, env):
        res = self.expr.evaluate(env)
        print(res)
        return res 
    
    def __str__(self):
        return f"print {self.expr}"
    

class Nop(NoOperation):
    '''
    It does not perform any operations.
    '''
    def __init__(self):
        pass

    def evaluate(self, env):
        return "Nop"
    
    def __str__(self):
        return "nop"