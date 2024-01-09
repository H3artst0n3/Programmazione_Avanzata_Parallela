# Angelica Rota SM3201142

from expressions import *

class Reciprocal(UnaryOp):
    '''
    Class representing reciprocal

    Methods:
        op:      reciprocal of an element
        __str__: string representation of reciprocal
    '''
    def op(self, *args):
        if self.args[0] == 0:
            raise DivisionByZero("Reciprocal division by zero not allowed")
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