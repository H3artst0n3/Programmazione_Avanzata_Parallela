# Angelica Rota SM3201142

from expressions import *

class IfStatement(TernaryOp):
    '''
    Representation of an if statement

    Methods:
        __init__: contidion, branch if condition is True, branch if condition is False
        evaluate: if condition evaluation returns a True value then if-yes is evaluated, otherwise if-no.
                  Returns the value of the branch that was evaluated.
        __str__ : string representation of if statement
    '''
    def __init__(self, args):
        super().__init__(args)
        self.cond = args[2]
        self.if_yes = args[1]
        self.if_no = args[0]

    def evaluate(self, env):
        if self.cond.evaluate(env):
            return self.if_yes.evaluate(env)
        else:
            return self.if_no.evaluate(env) 
    
    def __str__(self):
        return f"if {self.cond} {self.if_yes} {self.if_no}"

class WhileStatement(BinaryOp):
    '''
    Representation of a while loop.

    Methods:
        __init__: condition and expression in the while loop
        evaluate: evaluates cond, and if True, evaluates expr until cond becomes False.
        __str__ : string representation of while loops
    '''
    def __init__(self, args):
        super().__init__(args)
        self.cond = args[1]
        self.expr = args[0]
    
    def evaluate(self, env):
        while self.cond.evaluate(env):
            expr = self.expr.evaluate(env)      
        
        return expr
    
    def __str__(self):
        return f"while {self.cond} {self.expr}"
    
class ForStatement(QuaternaryOp):
    '''
    Representation of a for loop.

    Methods:
        __init__: counter, start of the for loop, end of the for loop, expression in the for loop
        evaluate: Evaluate expr several times with the value of i from start to end - 1 in increments of 1
        __str__ : string representation of for loop
    '''
    def __init__(self, args):
        super().__init__(args)
        self.i = args[3].name
        self.start = args[2]
        self.end = args[1]
        self.expr = args[0]
    
    def evaluate(self, env):
        # if the counter is not in the environment add it to it
        if self.i not in env:
            env[self.i] = 0

        # evaluation of start and end because they can be both expressions
        start = self.start.evaluate(env)
        end = self.end.evaluate(env)
        expr = None
        
        env[self.i] = start

        # executes the loop and evaluates the expressions within it
        for i in range(start, end, 1):
            env[self.i] = i
            expr = self.expr.evaluate(env)
        
        return expr
    
    def __str__(self):
        return f"for {self.i} {self.start} {self.end} {self.expr}"