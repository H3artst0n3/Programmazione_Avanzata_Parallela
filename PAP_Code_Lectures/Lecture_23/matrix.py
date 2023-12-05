class Matrix:
    def __init__(self, nrows, ncols, initial_value):
        self.nrows = nrows
        self.ncols = ncols
        # self.data = [initial_value for _ in range(nrows*ncols)]
        self.data = [[initial_value for _ in range(ncols)] for _ in range(nrows)]

    def get_at(self, i, j):
        # pos = i * self.ncols + j
        return self.data[i][j]
    
    def set_at(self, i, j, x):
        # pos = i*self.ncols + j
        self.data[i][j] = x
    
    # ritorna una nuova matrice
    def multiply(self, m):
        # assumiamo matrici quadrate compatibili
        n = self.rows
        res = Matrix(n, n, 0)
        for i in range(0, n):
            for j in range(0, n):    
                x = 0
                for k in range(0, n):
                    x += self.get_at(i, k) * m.get_at(k, j)
                res.set_at(i, j, x)
        return res

m = Matrix(3, 3, 0)
m1 = Matrix(3, 3, 1)
m2 = Matrix(3, 3, 1)

# for i in range(m.nrows):
#     for j in range(m.ncols):
#          m.set_at(i, j, 1)

# print(m.get_at(1,2))

M = m1.multiply(m2)
print(M.data)