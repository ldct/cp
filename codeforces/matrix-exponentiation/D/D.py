#!/usr/bin/env pypy3

class Matrix(list):
    MODULUS=10**9+7
    def __matmul__(self, B) :
        A = self
        return Matrix([[sum(A[i][k]*B[k][j] for k in range(len(B))) % Matrix.MODULUS
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

N, M, K = input().split(' ')
N = int(N)
M = int(M)
K = int(K)

adjacency = []
for _ in range(N):
    adjacency += [[0]*N]

for _ in range(M):
    a, b = input().split(' ')
    a = int(a)-1
    b = int(b)-1
    adjacency[a][b] = 1

if True:
    import random
    N = 100
    K = 10**9
    adjacency = []
    for _ in range(N):
        adjacency += [[random.choice([0, 1])]*N]

print("test generation done")


adjacency = Matrix(adjacency)**K

ret = 0
for i in range(N):
    for j in range(N):
        ret += adjacency[i][j]
        ret %= Matrix.MODULUS

print(ret)
