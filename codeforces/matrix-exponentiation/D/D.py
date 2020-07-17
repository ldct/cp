#!/usr/bin/env python3

import array

class SquareMatrix():
    MODULUS=10**9+7
    def __init__(self, N):
        self.N = N
        self.storage = array.array('q', [0]*(N*N))
        self.tmp = array.array('q', [0]*(N*N))
    def rmul(self, B):
        for i in range(N):
            for j in range(N):
                self.tmp[i*N+j] = 0
                for k in range(N):
                    self.tmp[i*N+j] += self.storage[i*N+k]*B.storage[k*N+j]
                    self.tmp[i*N+j] %= SquareMatrix.MODULUS
        self.storage, self.tmp = self.tmp, self.storage
    def lmul(self, B):
        for i in range(N):
            for j in range(N):
                self.tmp[i*N+j] = 0
                for k in range(N):
                    self.tmp[i*N+j] += B.storage[i*N+k]*self.storage[k*N+j]
                    self.tmp[i*N+j] %= SquareMatrix.MODULUS
        self.storage, self.tmp = self.tmp, self.storage

    def __pow__(self, n, modulus=None):
        assert(modulus is None)

        result = SquareMatrix.Identity(self.N)
        b = self
        while n > 0:
            if (n%2) == 0:
                b.rmul(b)
                n //= 2
            else:
                result.lmul(b)
                b.rmul(b)
                n //= 2
        return result

    @classmethod  
    def Identity(cls, size):
        ret = SquareMatrix(N)
        for i in range(N):
            ret.storage[i*N+i] = 1
        return ret

N, M, K = input().split(' ')
N = int(N)
M = int(M)
K = int(K)

adjacency = SquareMatrix(N)

for _ in range(M):
    a, b = input().split(' ')
    a = int(a)-1
    b = int(b)-1
    adjacency.storage[a*N+b] = 1

if False:
    import random
    N = 100
    K = 10**9
    adjacency = SquareMatrix(N)
    for i in range(N*N):
        adjacency.storage[i] = random.choice([0, 1])

adjacency = adjacency**K

ret = 0
for i in range(N):
    for j in range(N):
        ret += adjacency.storage[i*N+j]
        ret %= SquareMatrix.MODULUS

print(ret)
