#!/usr/bin/env python3

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

K, M, N = input().split(' ')

K = int(K)
M = int(M)
N = int(N)

adjacency = []
for _ in range(K*K):
    row = [0]*(K*K)
    adjacency += [row]

for _ in range(M):
    P, Q, R = input().split(' ')
    P = int(P)
    Q = int(Q)
    R = int(R)

    P -= 1
    Q -= 1
    R -= 1

    adjacency[P*K + Q][Q*K+R] = 1

if N == 1: 
    print(1)
elif N == 2:
    print(adjacency[0][0])
else:
    adjacency = Matrix(adjacency)**(N-2)

    ret = 0

    for p in [0]:
        for q in range(K):
            for r in range(K):
                for s in [0]:
                    ret += adjacency[p*K+q][r*K+s]
                    ret = ret % Matrix.MODULUS
    print(ret)

