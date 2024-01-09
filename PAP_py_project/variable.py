# Angelica Rota SM3201142

from expressions import *

class Alloc(UnaryOp):
    '''
    Makes the variable available for subsequent parts of the code.

    Methods:
        __init__: variable name
        evaluate: default variable value equals to zero
        __str__ : string representation of alloc
    '''
    def __init__(self, args):
        super().__init__(args)
        self.name = args[0].name
    
    def evaluate(self, env):
        env[self.name] = 0
    
    def __str__(self):
        return f"alloc {self.name}"
    

class Valloc(BinaryOp):
    '''
    Makes an array of n elements available for subsequent parts of the code.

    Methods:
        __init__: array name and its length 
        evaluate: default array values all zeros, returns the array
        __str__ : string representation of valloc
    '''
    def __init__(self, args):
        super().__init__(args)
        self.name = args[1].name
        self.n = args[0]

    def evaluate(self, env):
        # evaluate of n because it can be also an expression not only a costant
        n = self.n.evaluate(env)

        if n < 0:
            raise ValueException("Length must be non-negative")
        env[self.name] = [0] * n

        return env[self.name]

    def __str__(self):
        return f"valloc {self.name} {self.n}"
    

class Setq(BinaryOp):
    '''
    Sets the value of the variable x to the result of the expression expr.

    Methods:
        __init__: variable name and result of the expression
        evaluate: set the new value of the variable x and returns the new value
        __str__ : string representation of setq
    '''
    def __init__(self, args):
        super().__init__(args)
        self.name = args[1].name
        self.expr = args[0]

    def evaluate(self, env):
        value = self.expr.evaluate(env)
        
        if self.name in env:
            env[self.name] = value
            return env[self.name]
       
        raise MissingVariableException("Setq can't find the variable.")

    def __str__(self):
        return f"setq {self.name} {self.expr}"
    

class Setv(TernaryOp):
    '''
    Sets the value of the n-th position of the indicated array.

    Methods:
        __init__: array name, n-th position and value returned by expr
        evaluate: returns the new value of x at position n (arrays are indexed from zero)
        __str__ : string representation of setv
    '''
    def __init__(self, args):
        super().__init__(args)
        self.name = args[2].name
        self.n = args[1]
        self.expr = args[0]

    def evaluate(self, env):
        # evaluation of expr and n because they can be both expressions
        value = self.expr.evaluate(env)
        n = self.n.evaluate(env)

        if self.name in env and isinstance(env[self.name], list) and n < len(env[self.name]):
            # If the variable already exists in the environment and is a list and the position is valid
            env[self.name][n] = value
            return env[self.name][n]
        
        if not self.name in env:
            return MissingVariableException("Setv can't find the variable.")
        elif not isinstance(env[self.name], list):
            return TypeException("Variable not a list")
        
        return IndexException("Invalid index")
    
    def __str__(self):
        return f"setv {self.name} {self.n} {self.expr}"