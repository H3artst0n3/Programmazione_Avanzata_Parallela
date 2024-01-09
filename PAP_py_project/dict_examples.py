# Angelica Rota SM3201142

from binary import *
from unary import *
from boolean import *
from variable import *
from sequences import *
from cond_iter import *
from subroutine import *
from extra_functions import *

'''
Dictionary mapping operators to their respective operation classes.

Rows:
1- Binary Operations
2- Unary Operations
3- Boolean Operations
4- Variable Definitions
5- Management of sequences of expressions
6- Conditionals and iterations
7- Subroutine
8- Extra functions
'''
d = {"+": Addition, "*": Multiplication, "**": Power, "-": Subtraction, "/": Division, "%": Modulus, 
     "1/": Reciprocal, "abs": AbsoluteValue,
     ">": Greater, ">=": GreaterEqual, "=": Equal, "!=": NotEqual, "<": Less, "<=": LessEqual, 
     "alloc": Alloc, "valloc": Valloc, "setq": Setq, "setv": Setv,
     "prog2": Prog2, "prog3": Prog3, "prog4": Prog4,
     "if": IfStatement, "while": WhileStatement, "for": ForStatement,
     "defsub": Subroutine, "call": Call,
     "print": Print, "nop": Nop}


###############################################################
########################### Examples ##########################
###############################################################
'''
Simple example addition in RPN.

Expected output:
(+ 3 2)
5
'''
example = "2 3 +"
e = Expression.from_program(example, d)
print(e)
res = e.evaluate({})
print(f"{res}\n")



'''
Test example given by the exercise.

Expected output:
(1/ (+ (1/ y) (** 2 (abs (/ (- 5 6) (* x (+ 3 2)))))))
0.84022932953024
'''
example_v2 = "2 3 + x * 6 5 - / abs 2 ** y 1/ + 1/"
e_v2 = Expression.from_program(example_v2, d)
print(e_v2)
res_v2 = e_v2.evaluate({"x": 3, "y": 7})
print(f"{res_v2}\n")



'''
Simple check for booleans operations.

Expected output:
(= 3 3)
True
'''
example_v3 = "3 3 ="
e_v3 = Expression.from_program(example_v3, d)
print(e_v3)
res_v3 = e_v3.evaluate({})
print(f"{res_v3}\n")



'''
Simple check for variable definition.

Expected output:
valloc x (+ 3 2)
[0, 0, 0, 0, 0]
'''
example_v4 = "2 3 + x valloc"
e_v4 = Expression.from_program(example_v4, d)
print(e_v4)
res_v4 = e_v4.evaluate({})
print(f"{res_v4}\n")



'''
Simple check for management of sequences of expressions.

Expected output:
prog2 alloc x (+ x 2)
2
'''
example_v5 = "2 x + x alloc prog2"
e_v5 = Expression.from_program(example_v5, d)
print(e_v5)
res_v5 = e_v5.evaluate({})
print(f"{res_v5}\n")



'''
Simple check for conditional.

Expected output:
prog2 alloc x if (= 0 x) (+ 5 x) (+ 1 x)
5
'''
example_v6 = "x 1 + x 5 + x 0 = if x alloc prog2"
e_v6 = Expression.from_program(example_v6, d)
print(e_v6)
res_v6 = e_v6.evaluate({})
print(f"{res_v6}\n")



'''
Simple check for "while" statement. 
First code example given in the project outline.

Expected output:
prog2 alloc x while (> 10 x) setq x (+ 1 x)
10
''' 
example_v7 = "x 1 + x setq x 10 > while x alloc prog2"
e_v7 = Expression.from_program(example_v7, d)
print(e_v7)
res_v7 = e_v7.evaluate({})
print(f"{res_v7}\n")



'''
Simple check for "for" statement.
Second code example given in the project outline.

Expected output:
prog3 valloc v 10 for i 0 10 setv v i (* i i) print v
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Note:
print(res_v8) is commented because there is a print in the expression.
'''
example_v8 = "v print i i * i v setv 10 0 i for 10 v valloc prog3"
e_v8 = Expression.from_program(example_v8, d)
print(e_v8)
res_v8 = e_v8.evaluate({})
# print(res_v8)
print()



'''
Simple check for subroutine.
Third code example given in the project outline.

Expected output:
prog4 defsub f setq x (+ 4 x) alloc x call f print x
4
Note:
print(res_v9) is commented because there is a print in the expression.
''' 
example_v9 = "x print f call x alloc x 4 + x setq f defsub prog4"
e_v9 = Expression.from_program(example_v9, d)
print(e_v9)
res_v9 = e_v9.evaluate({})
# print(res_v9)
print()

'''
Program that finds the divisors of 783.
Fourth code example given in the project outline.

Expected output:
prog3 alloc x setq x 783 for i 2 1000 if (= 0 (mod x i)) print i nop
3
9
27
29
87
261
783
Nop
''' 
example_v10 = "nop i print i x % 0 = if 1000 2 i for 783 x setq x alloc prog3"
e_v10 = Expression.from_program(example_v10, d)
print(e_v10)
res_v10 = e_v10.evaluate({})
print(f"{res_v10}\n")



'''
Program that prints all prime numbers less than 100.
Fifth code example given in the project outline.

Expected output:
for x 2 100 prog4 alloc prime setq prime (= 0 0) for i 2 (- x 1) if (= 0 (mod x i)) setq prime (!= 0 0) nop if prime print x nop
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
Nop
''' 
example_v11 = "nop x print prime if nop 0 0 != prime setq i x % 0 = if 1 x - 2 i for 0 0 = prime setq prime alloc prog4 100 2 x for"
e_v11 = Expression.from_program(example_v11, d)
print(e_v11)
res_v11 = e_v11.evaluate({})
print(res_v11)