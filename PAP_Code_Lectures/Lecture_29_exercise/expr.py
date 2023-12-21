# Angelica Rota SM320142

# custom exception for an empty stack
class EmptyStackException(Exception):
    pass


class Stack:
    '''
    Stack class to simulate stack operations

    Methods:
        __init__: data structure to store stack elements
        push:     adds element to the top of the stack
        pop:      picks the top element and returns it
        __str__:  string representation of the stack
    '''
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.data == []:
            # raise exception if pop is called on an empty stack
            raise EmptyStackException
        
        # retrieve the top element and shorten stack length
        res = self.data[-1]
        self.data = self.data[0:-1]
        return res

    def __str__(self):
        return " ".join([str(s) for s in self.data])



class Expression:
    '''
    Base class representing an expression

    Methods:
        from_program: takes a sequence of tokens and constructs an expression 
        tree according to the Reverse Polish Notation (RPN)
    '''
    def __init__(self):
        # force subclasses to implement this method
        raise NotImplementedError()

    @classmethod
    def from_program(cls, text, dispatch):
        # create a stack instance and spit the input into tokens
        stack = Stack()
        tokens = text.split()

        for token in tokens:
            if token in dispatch:
                # fetch the corresponding operation class from the dispatch dictionary
                op_class = dispatch[token]

                # check if the operation is a subclass of Operation
                if issubclass(op_class, Operation):
                    # if it is a unary operation pop of one element 
                    if op_class.arity == 1:
                        arg = stack.pop()
                        stack.push(op_class([arg]))
                    # if it is a binary operation pop of two elements
                    elif op_class.arity == 2:
                        arg2 = stack.pop()
                        arg1 = stack.pop()
                        stack.push(op_class([arg1, arg2]))
                # if it is not an operation, it's a variable or a constant
                else:
                    stack.push(op_class())
            # if the token is not in the dispatch, it's a value (constant or variable)
            else:
                try:
                    value = int(token)

                    # push as a constant
                    stack.push(Constant(value))
                except ValueError:
                    # push as a variable 
                    stack.push(Variable(token))

        # return the final resault of the expression
        return stack.pop()

    def evaluate(self, env):
        # force subclasses to implement this method
        raise NotImplementedError("Subclass must implement evaluate method")
    
    def __str__(self):
        # force subclasses to implement this method
        raise NotImplementedError("Subclass must implement __str__ method")


# custom exception for an empty stack
class MissingVariableException(Exception):
    pass


class Variable(Expression):
    '''
    Variable class representing a variable in the expression

    Methods:
        __init__: variable name
        evaluate: retrieve value from the environment or raise exception if variable is missing
        __str__ : string representation of the variable
    '''
    def __init__(self, name):
        self.name = name

    def evaluate(self, env):
        if self.name in env:
            return env[self.name]
        else:
            raise MissingVariableException()

    def __str__(self):
        return self.name


class Constant(Expression):
    '''
    Constant class representing a constant value in the expression

    Methods:
        __init__: constant value
        evaluate: return the constant value
        __str__ : string representation of the constant
    '''
    def __init__(self, value):
        self.value = value

    def evaluate(self, env):
        return self.value

    def __str__(self):
        return str(self.value)


class Operation(Expression):
    '''
    Base class for operations

    Methods:
        __init__: list of arguments for the operation
        evaluate: evaluate arguments in the environment and apply the operation on the evaluated arguments
    '''
    def __init__(self, args):
        self.args = args

    def evaluate(self, env):
        evaluated_args = [arg.evaluate(env) for arg in self.args]
        return self.op(*evaluated_args)

    def op(self, *args):
        # force subclasses to implement this method
        raise NotImplementedError("Subclass must implement op method")


class BinaryOp(Operation):
    '''
    Class representing binary operations
    '''
    arity = 2

class UnaryOp(Operation):
    '''
    Class representing unary operations
    '''
    arity = 1


######################################################################
########## Start of the list of different operation classes ##########
######################################################################

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

######################################################################
########### End of the list of different operation classes ###########
######################################################################


# dictionary mapping operators to their respective operation classes
d = {"+": Addition, "*": Multiplication, "**": Power, "-": Subtraction,
     "/": Division, "%": Modulus, "1/": Reciprocal, "abs": AbsoluteValue}

# simple example expression in RPN
example = "2 3 +"
e = Expression.from_program(example, d)
print(e)
res = e.evaluate({})
print(res)

# expected output:
# (+ 3 2)
# 5

# test example given by the exercise
example_v2 = "2 3 + x * 6 5 - / abs 2 ** y 1/ + 1/"
e_v2 = Expression.from_program(example_v2, d)
print(e_v2)
res = e_v2.evaluate({"x": 3, "y": 7})
print(res)

# expected output:
# (1/ (+ (1/ y) (** 2 (abs (/ (- 5 6) (* x (+ 3 2)))))))
# 0.84022932953024
