# Angelica Rota SM3201142

from expressions import *

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