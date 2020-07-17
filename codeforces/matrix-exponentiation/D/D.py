#!/usr/bin/env pypy3

import array

class SquareMatrix():
    MODULUS=10**9+7
    def __init__(self, N):
        self.N = N
        self.storage = array.array('i', [0]*(N*N))
        self.tmp = array.array('i', [0]*(N*N))
    def rmul(self, B):
        for i in range(N*N):
            self.tmp[i] = 0
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    self.tmp[i*N+k] = (self.tmp[i*N+k] + (self.storage[i*N+j]*B.storage[j*N+k]) % SquareMatrix.MODULUS) % SquareMatrix.MODULUS
        self.storage, self.tmp = self.tmp, self.storage
    def lmul(self, B):
        for i in range(N*N):
            self.tmp[i] = 0
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    self.tmp[i*N+k] = (self.tmp[i*N+k] + (B.storage[i*N+j]*self.storage[j*N+k]) % SquareMatrix.MODULUS) % SquareMatrix.MODULUS
        self.storage, self.tmp = self.tmp, self.storage

    def __pow__(self, n, modulus=None):
        assert(modulus is None)

        result = SquareMatrix.Identity(self.N)
        b = self
        while n > 0:
            if (n%2) == 1: result.lmul(b)
            b.rmul(b)
            n //= 2
        return result

    @classmethod  
    def Identity(cls, size):
        ret = SquareMatrix(N)
        for i in range(N):
            ret.storage[i*N+i] = 1
        return ret

if True:
    import random
    N = 100
    K = 2
    adjacency = SquareMatrix(N)
    for i in range(N*N):
        adjacency.storage[i] = random.choice([1])
    adjacency = adjacency**K
    exit(0)
else:
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

adjacency = adjacency**K

ret = 0
for i in range(N):
    for j in range(N):
        ret += adjacency.storage[i*N+j]
        ret %= SquareMatrix.MODULUS

print(ret)