# Angelica Rota SM3201142

from operations import *
from expressions import *

# dictionary mapping operators to their respective operation classes
d = {"+": Addition, "*": Multiplication, "**": Power, "-": Subtraction,
     "/": Division, "%": Modulus, "1/": Reciprocal, "abs": AbsoluteValue,
     ">": Greater, ">=": GreaterEqual, "=": Equal, "!=": NotEqual, "<": Less,
     "<=": LessEqual, "alloc": Alloc, "valloc": Valloc, "setq": Setq, "setv": Setv,
     "prog2": Prog2, "prog3": Prog3, "prog4": Prog4}

# # simple example expression in RPN
# example = "2 3 +"
# e = Expression.from_program(example, d)
# print(e)
# res = e.evaluate({})
# print(res)

# expected output:
# (+ 3 2)
# 5

# # test example given by the exercise
# example_v2 = "2 3 + x * 6 5 - / abs 2 ** y 1/ + 1/"
# e_v2 = Expression.from_program(example_v2, d)
# print(e_v2)
# res_v2 = e_v2.evaluate({"x": 3, "y": 7})
# print(res_v2)

# expected output:
# (1/ (+ (1/ y) (** 2 (abs (/ (- 5 6) (* x (+ 3 2)))))))
# 0.84022932953024

# # simple check for booleans operations
# example_v3 = "3 3 ="
# e_v3 = Expression.from_program(example_v3, d)
# print(e_v3)
# res_v3 = e_v3.evaluate({})
# print(res_v3)

# # simple check for variable definition
# example_v4 = "3 2 + 2 x setv"
# e_v4 = Expression.from_program(example_v4, d)
# print(e_v4)
# res_v4 = e_v4.evaluate({})
# print(res_v4)

# simple check for management of sequences of expressions
example_v5 = "3 2 + 1 x setv 5 x valloc prog2"
e_v5 = Expression.from_program(example_v5, d)
print(e_v5)
res_v5 = e_v5.evaluate({})
print(res_v5)