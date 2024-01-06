# Angelica Rota SM3201142

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
    
class Alloc(UnaryOp):
    def __init__(self, *args):
        self.name = args[0][0].name
    
    def evaluate(self, env):
        env[self.name] = 0
        return env[self.name]
    
    def __str__(self):
        return f"alloc {self.name}"
    
class Valloc(BinaryOp):
    def __init__(self, *args):
        self.name = args[0][1]
        self.n = args[0][0].evaluate({})

    def evaluate(self, env):
        env[self.name] = [0] * self.n
        print("valloc")
        print(f"nome: {self.name}, N: {self.n}")
        print(f"env: {env.get(self.name)}, is_list: {isinstance(env.get(self.name), list)}")
        print(env[self.name])
        return env[self.name]

    def __str__(self):
        return f"valloc {self.name} {self.n}"
    
class Setq(BinaryOp):
    def __init__(self, *args):
        self.name = args[0][1]
        self.expr = args[0][0]

    def evaluate(self, env):
        value = self.expr.evaluate(env)
        env[self.name] = value
        return env[self.name]
    
    def __str__(self):
        return f"setq {self.name} {self.expr}"
    
class Setv(TernaryOp):
    def __init__(self, *args):
        self.name = args[0][2]
        self.n = args[0][1].evaluate({})
        self.expr = args[0][0]

    def evaluate(self, env):
        value = self.expr.evaluate(env)

        print("Setv")
        print(f"nome: {self.name}, N: {self.n}")
        print(f"env: {env.get(self.name)}, is_list: {isinstance(env.get(self.name), list)}")
        if self.name in env and isinstance(env[self.name], list) and 0 <= self.n < len(env[self.name]):
            # Se la variabile esiste già nell'ambiente ed è una lista e la posizione è valida
            env[self.name][self.n] = value
            return env[self.name]
        else:
            return None
    
    def __str__(self):
        return f"setv {self.name} {self.n} {self.expr}"
    

################################################################
############ Management of sequences of expressions ############
################################################################

class Prog2(BinaryOp):
    def __init__(self, *args):
        self.expr1 = args[0][1]
        self.expr2= args[0][0]
    
    def evaluate(self, env):
        self.expr1.evaluate(env)
        return self.expr2.evaluate(env)
    
    def __str__(self):
        return f"prog2 {self.expr1} {self.expr2}"


class Prog3(TernaryOp):
    def __init__(self, *args):
        self.expr1 = args[0][2]
        self.expr2 = args[0][1]
        self.expr3= args[0][0]
    
    def evaluate(self, env):
        self.expr1.evaluate(env)
        self.expr2.evaluate(env)
        return self.expr3.evaluate(env)
    
    def __str__(self):
        return f"prog3 {self.expr1} {self.expr2} {self.expr3}"
    

class Prog4(QuaternaryOp):
    def __init__(self, *args):
        self.expr1 = args[0][3]
        self.expr2 = args[0][2]
        self.expr3 = args[0][1]
        self.expr4= args[0][0]
    
    def evaluate(self, env):
        self.expr1.evaluate(env)
        self.expr2.evaluate(env)
        self.expr3.evaluate(env)
        return self.expr4.evaluate(env)
    
    def __str__(self):
        return f"prog4 {self.expr1} {self.expr2} {self.expr3} {self.expr4}"