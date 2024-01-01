from expressions import *

################################################################
################### List of Binary Operations ##################
################################################################

class Addition(BinaryOp):
    '''
    Class representing addition

    Methods:
        op:      sum of two elements
        __str__: string representation of addition
    '''
    def op(self, *args):
        return args[1] + args[0]

    def __str__(self):
        return f"(+ {self.args[1]} {self.args[0]})"


class Subtraction(BinaryOp):
    '''
    Class representing subtraction

    Methods:
        op:      difference between two elements
        __str__: string representation of subtraction
    '''
    def op(self, *args):
        return args[1] - args[0]

    def __str__(self):
        return f"(- {self.args[1]} {self.args[0]})"


class Division(BinaryOp):
    '''
    Class representing division

    Methods:
        op:      division between two elements
        __str__: string representation of division
    '''
    def op(self, *args):
        return args[1] / args[0]

    def __str__(self):
        return f"(/ {self.args[1]} {self.args[0]})"


class Multiplication(BinaryOp):
    '''
    Class representing multiplication

    Methods:
        op:      multiplication between two elements
        __str__: string representation of multiplication
    '''
    def op(self, *args):
        return args[1] * args[0]

    def __str__(self):
        return f"(* {self.args[1]} {self.args[0]})"


class Power(BinaryOp):
    '''
    Class representing power

    Methods:
        op:      power between two elements
        __str__: string representation of power
    '''
    def op(self, *args):
        return args[1] ** args[0]

    def __str__(self):
        return f"(** {self.args[1]} {self.args[0]})"


class Modulus(BinaryOp):
    '''
    Class representing modulus

    Methods:
        op:      modulus between two elements
        __str__: string representation of modulus
    '''
    def op(self, *args):
        return args[1] % args[0]

    def __str__(self):
        return f"(mod {self.args[1]} {self.args[0]})"

class Greater(BinaryOp):
    '''
    Class representing greater

    Methods:
        op:      check if one element is greater then the other
        __str__: string representation of greater
    '''
    def op(self, *args):
        return args[1] > args[0]

    def __str__(self):
        return f"(> {self.args[1]} {self.args[0]})"


class GreaterEqual(BinaryOp):
    '''
    Class representing greater

    Methods:
        op:      check if one element is greater then the other
        __str__: string representation of greater
    '''
    def op(self, *args):
        return args[1] >= args[0]

    def __str__(self):
        return f"(>= {self.args[1]} {self.args[0]})"


class Equal(BinaryOp):
    '''
    Class representing greater

    Methods:
        op:      check if one element is greater then the other
        __str__: string representation of greater
    '''
    def op(self, *args):
        return args[1] == args[0]

    def __str__(self):
        return f"(= {self.args[1]} {self.args[0]})"


class NotEqual(BinaryOp):
    '''
    Class representing greater

    Methods:
        op:      check if one element is greater then the other
        __str__: string representation of greater
    '''
    def op(self, *args):
        return args[1] != args[0]

    def __str__(self):
        return f"(!= {self.args[1]} {self.args[0]})"


class Less(BinaryOp):
    '''
    Class representing greater

    Methods:
        op:      check if one element is greater then the other
        __str__: string representation of greater
    '''
    def op(self, *args):
        return args[1] < args[0]

    def __str__(self):
        return f"(< {self.args[1]} {self.args[0]})"


class LessEqual(BinaryOp):
    '''
    Class representing greater

    Methods:
        op:      check if one element is greater then the other
        __str__: string representation of greater
    '''
    def op(self, *args):
        return args[1] <= args[0]

    def __str__(self):
        return f"(<= {self.args[1]} {self.args[0]})"

################################################################
################### List of Unary Operations ###################
################################################################

class Reciprocal(UnaryOp):
    '''
    Class representing reciprocal

    Methods:
        op:      reciprocal of an element
        __str__: string representation of reciprocal
    '''
    def op(self, *args):
        return 1 / args[0]

    def __str__(self):
        return f"(1/ {self.args[0]})"


class AbsoluteValue(UnaryOp):
    '''
    Class representing absolute value

    Methods:
        op:      absolute value of an element
        __str__: string representation of absolute value
    '''
    def op(self, *args):
        return abs(args[0])

    def __str__(self):
        return f"(abs {self.args[0]})"

################################################################
###################### Variable definition #####################
################################################################
    
class Alloc(Expression):
    def __init__(self, name):
        self.name = name
    
    def evaluate(self, env):
        env[self.name] = 0
        return env[self.name]
    
    def __str__(self):
        return f"alloc {self.name}"
    
class Valloc(Expression):
    def __init__(self, name, n):
        self.name = name
        self.n = n.evaluate({})

    def evaluate(self, env):
        env[self.name] = [0] * self.n
        return env[self.name]

    def __str__(self):
        return f"valloc {self.name} {self.n}"
    
class Setq(Expression):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

    def evaluate(self, env):
        value = self.expr.evaluate(env)
        env[self.name] = value
        return env[self.name]
    
    def __str__(self):
        return f"setq {self.name} {self.expr}"
    
class Setv(Expression):
    def __init__(self, n, name, expr):
        self.n = n.evaluate({})
        self.name = name
        self.expr = expr

    def evaluate(self, env):
        value = self.expr.evaluate(env)

        if self.name in env:
            env[self.name][self.n] = value
            return env[self.name]
    
    def __str__(self):
        return f"setv {self.n} {self.name} {self.expr}"