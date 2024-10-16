from ctypes import *


code = cdll.LoadLibrary("./libmatrix.dll")

code.make_random_matrix.argtypes = [c_int]
code.make_random_matrix.restype = POINTER(c_float)
code.make_zero_matrix.argtypes = [c_int]
code.make_zero_matrix.restype = POINTER(c_float)

code.omp_blocked_multiply.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float), c_int]

n = 10
A = code.make_random_matrix(n)
B = code.make_random_matrix(n)
C = code.make_zero_matrix(n)

code.omp_blocked_multiply(A, B, C, n)
code.print_matrix(C, n, 0)
# for i in range(n):
#     for j in range(n):
#         print(f"{C[i * n + j]} ")
#     print("\n")

# print(f"A[2, 4] = {A[2*n +4]}")