# Angelica Rota SM3201142

from expressions import *

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
        if self.args[0] == 0:
            raise DivisionByZero("Division by zero not allowed")
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
        if self.args[0] == 0:
            raise DivisionByZero("Modulus operation with divisor zero not allowed")
        return args[1] % args[0]

    def __str__(self):
        return f"(mod {self.args[1]} {self.args[0]})"
