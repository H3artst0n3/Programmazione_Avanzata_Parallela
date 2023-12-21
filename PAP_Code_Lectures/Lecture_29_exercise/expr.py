class EmptyStackException(Exception):
    pass


class Stack:

    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.data == []:
            raise EmptyStackException
        res = self.data[-1]
        self.data = self.data[0:-1]
        return res

    def __str__(self):
        return " ".join([str(s) for s in self.data])


class Expression:

    def __init__(self):
        raise NotImplementedError()

    @classmethod
    def from_program(cls, text, dispatch):
        stack = Stack()
        tokens = text.split()

        for token in tokens:
            if token in dispatch:
                op_class = dispatch[token]
                if issubclass(op_class, Operation):
                    if op_class.arity == 1:
                        arg = stack.pop()
                        stack.push(op_class(arg))
                    elif op_class.arity == 2:
                        arg2 = stack.pop()
                        arg1 = stack.pop()
                        op_class = op_class([arg1, arg2])
                        stack.push(op_class.op(arg1, arg2))
                else:
                    stack.push(op_class())
            else:
                stack.push(Constant(token))

        return stack.pop()
    
    def evaluate(self, env):
        raise NotImplementedError()


class MissingVariableException(Exception):
    pass


class Variable(Expression):

    def __init__(self, name):
        self.name = name

    def evaluate(self, env):
        if self.name in env:
            return env[self.name]
        else:
            raise MissingVariableException

    def __str__(self):
        return self.name


class Constant(Expression):

    def __init__(self, value):
        self.value = value

    def evaluate(self, env):
        return self.value

    def __str__(self):
        return str(self.value)
    
    def __add__(self, y):
        return self.value + y.value
    
    def __mul__(self, y):
        self.value *= y.value
        return self.value


class Operation(Expression):

    def __init__(self, args):
        self.args = args

    def evaluate(self, env):
        pass

    def op(self, *args):
        raise NotImplementedError()

    def __str__(self):
        pass


class BinaryOp(Operation):
    arity = 2
    pass


class UnaryOp(Operation):
    arity = 1
    pass


class Addition(BinaryOp):
    def op(self, x, y):
        return x + y
    
    def __str__(self):
        return f"(+ {self.args[0]} {self.args[1]} )"


class Subtraction(BinaryOp):
    def op(self, x, y):
        return x - y
    
    def __str__(self):
        return f"({self.args[0]} - {self.args[1]})"


class Division(BinaryOp):
    def op(self, x, y):
        return x / y
    
    def __str__(self):
        return f"({self.args[0]} / {self.args[1]})"



class Multiplication(BinaryOp):
    def op(self, x, y):
        return x * y
    
    def __str__(self):
        return f"({self.args[0]} {self.args[1]} * )"



class Power(BinaryOp):
    def op(self, x, y):
        return x ** y
    
    def __str__(self):
        return f"({self.args[0]} ** {self.args[1]})"



class Modulus(BinaryOp):
    def op(self, x, y):
        return x % y
    
    def __str__(self):
        return f"({self.args[0]} % {self.args[1]})"



class Reciprocal(UnaryOp):
    def op(self, x):
        return 1/x
    
    def __str__(self):
        return f"(1/ {self.args})"



class AbsoluteValue(UnaryOp):
    def op(self, x):
        return abs(x)
    
    def __str__(self):
        return f"abs {self.args}"


d = {"+": Addition, "*": Multiplication, "**": Power, "-": Subtraction,
     "/": Division, "1/": Reciprocal, "abs": AbsoluteValue}
example = "2 3 + x * 6 5 - / abs 2 ** y 1/ + 1/"
# example = "2 3 +"
e = Expression.from_program(example, d)
print(e)
# res = e.evaluate({"x": 3, "y": 7})
# print(res)

# Ouput atteso:
# (1/ (+ (1/ y) (** 2 (abs (/ (- 5 6) (* x (+ 3 2)))))))
# 0.84022932953024

# Note:
# possiamo usare la conversione float o int per verificare se abbiamo un numero, una variabile o una operazione
# volendo come cosa aggiuntiva possiamo generare un file c che poi possiamo compilare