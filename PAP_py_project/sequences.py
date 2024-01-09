# Angelica Rota SM3201142

from expressions import *

class Prog2(BinaryOp):
    '''
    Evaluate the previous two expressions and returns the value of the latter popped expression from the stack.

    Methods:
        __init__: expr1 and expr2
        evaluate: evaluation of all the expression, returns the value of the latter popped expression from the stack.
        __str__ : string representation of prog2
    '''
    def __init__(self, args):
        super().__init__(args)
        self.expr1 = args[1]
        self.expr2= args[0]
    
    def evaluate(self, env):
        self.expr1.evaluate(env)
        return self.expr2.evaluate(env)
    
    def __str__(self):
        return f"prog2 {self.expr1} {self.expr2}"


class Prog3(TernaryOp):
    '''
    Evaluate the previous three expressions and returns the value of the latter popped expression from the stack.

    Methods:
        __init__: expr1, expr2 and expr3
        evaluate: evaluation of all the expression, returns the value of the latter popped expression from the stack.
        __str__ : string representation of prog3
    '''
    def __init__(self, args):
        super().__init__(args)
        self.expr1 = args[2]
        self.expr2 = args[1]
        self.expr3= args[0]
    
    def evaluate(self, env):
        self.expr1.evaluate(env)
        self.expr2.evaluate(env)
        return self.expr3.evaluate(env)
    
    def __str__(self):
        return f"prog3 {self.expr1} {self.expr2} {self.expr3}"
    

class Prog4(QuaternaryOp):
    '''
    Evaluate the previous four expressions and returns the value of the latter popped expression from the stack.

    Methods:
        __init__: expr1, expr2, expr3 and expr4
        evaluate: evaluation of all the expression, returns the value of the latter popped expression from the stack.
        __str__ : string representation of prog4
    '''
    def __init__(self, args):
        super().__init__(args)
        self.expr1 = args[3]
        self.expr2 = args[2]
        self.expr3 = args[1]
        self.expr4= args[0]
    
    def evaluate(self, env):
        self.expr1.evaluate(env)
        self.expr2.evaluate(env)
        self.expr3.evaluate(env)
        return self.expr4.evaluate(env)
    
    def __str__(self):
        return f"prog4 {self.expr1} {self.expr2} {self.expr3} {self.expr4}"