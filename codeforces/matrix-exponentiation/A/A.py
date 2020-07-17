#!/usr/bin/env python3

class Matrix(list):
    def __matmul__(self, B) :
        A = self
        return Matrix([[sum(A[i][k]*B[k][j] for k in range(len(B)))
                    for j in range(len(B[0])) ] for i in range(len(A))])

    def __pow__(self, n, modulus=None):
        assert(modulus is None)

        result = Matrix.Identity(len(self))
        b = self
        while n > 0:
            if (n%2) == 0:
                b = b @ b
                n //= 2
            else:
                result = b @ result
                b = b @ b
                n //= 2
        return result

    @classmethod  
    def Identity(cls, size):
        size = range(size)
        return Matrix([[(i==j)*1 for i in size] for j in size])

N, P = input().split(' ')
N = int(N)
P = float(P)

M = Matrix([[1-P, P], [P, 1-P]])**N
vec = M @ Matrix([[1.0], [0.0]])

print(vec[0][0])