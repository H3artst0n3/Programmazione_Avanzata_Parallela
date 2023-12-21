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
                        stack.push(op_class([arg]))
                    elif op_class.arity == 2:
                        arg2 = stack.pop()
                        arg1 = stack.pop()
                        stack.push(op_class([arg1, arg2]))
                else:
                    stack.push(op_class())
            else:
                try:
                    value = int(token)
                    stack.push(Constant(value))
                except ValueError:
                    stack.push(Variable(token))

        return stack.pop()

    def evaluate(self, env):
        raise NotImplementedError("Subclass must implement evaluate method")
    
    def __str__(self):
        raise NotImplementedError("Subclass must implement __str__ method")


class MissingVariableException(Exception):
    pass


class Variable(Expression):

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

    def __init__(self, value):
        self.value = value

    def evaluate(self, env):
        return self.value

    def __str__(self):
        return str(self.value)


class Operation(Expression):

    def __init__(self, args):
        self.args = args

    def evaluate(self, env):
        evaluated_args = [arg.evaluate(env) for arg in self.args]
        return self.op(*evaluated_args)

    def op(self, *args):
        raise NotImplementedError("Subclass must implement op method")

    def __str__(self):
        pass


class BinaryOp(Operation):
    arity = 2

class UnaryOp(Operation):
    arity = 1


class Addition(BinaryOp):
    def op(self, *args):
        return args[1] + args[0]

    def __str__(self):
        return f"(+ {self.args[1]} {self.args[0]})"


class Subtraction(BinaryOp):
    def op(self, *args):
        return args[1] - args[0]

    def __str__(self):
        return f"(- {self.args[1]} {self.args[0]})"


class Division(BinaryOp):
    def op(self, *args):
        return args[1] / args[0]

    def __str__(self):
        return f"(/ {self.args[1]} {self.args[0]})"


class Multiplication(BinaryOp):
    def op(self, *args):
        return args[1] * args[0]

    def __str__(self):
        return f"(* {self.args[1]} {self.args[0]})"


class Power(BinaryOp):
    def op(self, *args):
        return args[1] ** args[0]

    def __str__(self):
        return f"(** {self.args[1]} {self.args[0]})"


class Modulus(BinaryOp):
    def op(self, *args):
        return args[1]%args[0]

    def __str__(self):
        return f"(mod {self.args[1]} {self.args[0]})"


class Reciprocal(UnaryOp):
    def op(self, *args):
        return 1/args[0]

    def __str__(self):
        return f"(1/ {self.args[0]})"


class AbsoluteValue(UnaryOp):
    def op(self, *args):
        return abs(args[0])

    def __str__(self):
        return f"(abs {self.args[0]})"


d = {"+": Addition, "*": Multiplication, "**": Power, "-": Subtraction,
     "/": Division, "1/": Reciprocal, "abs": AbsoluteValue}
example = "2 3 + x * 6 5 - / abs 2 ** y 1/ + 1/"
# example = "2 3 +"
e = Expression.from_program(example, d)
print(e)
res = e.evaluate({"x": 3, "y": 7})
print(res)

# Ouput atteso:
# (1/ (+ (1/ y) (** 2 (abs (/ (- 5 6) (* x (+ 3 2)))))))
# 0.84022932953024
