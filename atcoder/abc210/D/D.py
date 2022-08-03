#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import math, copy, random

def make_fill(N, M, val):
    ret = []
    for _ in range(N):
        ret += [[val]*M]
    return ret

class Sparse2:
    def __init__(self, mat):

        self._mat = mat

        N = len(mat)
        M = len(mat[0])

        lN = 1+math.floor(math.log(N,2))
        lM = 1+math.floor(math.log(M,2))

        self.table = []

        for i in range(lN):
            row = []
            for j in range(lM):
                if (i, j) == (0, 0):
                    row += [copy.deepcopy(mat)]
                else:
                    row += [make_fill(N, M, -1)]
            self.table += [row]

        for ir in range(N):
            for jc in range(1, lM):
                for ic in range(M-2**(jc-1)):
                    self.table[0][jc][ir][ic]=min(self.table[0][jc-1][ir][ic],self.table[0][jc-1][ir][ic+2**(jc-1)])

        for jr in range(1, lN):
            for ir in range(N-2**(jr-1)):
                for jc in range(lM):
                    for ic in range(M):
                        self.table[jr][jc][ir][ic] = min(
                            self.table[jr-1 ][jc ][ir][ic ],
                            self.table[jr-1 ][jc][ir+2**(jr-1)][ic]
                        )

    def check(self):
        N = len(self._mat)
        M = len(self._mat[0])

        for x1 in range(N):
            for x2 in range(x1, N):
                for y1 in range(M):
                    for y2 in range(y1, M):
                        s.query(x1, y1, x2, y2)

    def query_slow(self, x1, y1, x2, y2):
        ret = float("inf")
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                ret = min(ret, self._mat[x][y])
        return ret


    def query(self, x1, y1, x2, y2):
        if not (x1 <= x2): return float("inf")
        if not (y1 <= y2): return float("inf")

        lenx=x2-x1+1
        kx=math.floor(math.log(lenx, 2))
        leny=y2-y1+1
        ky=math.floor(math.log(leny, 2))

        subtable = self.table[kx][ky]

        if not (x1 <= x2 < len(subtable)): return float("inf")
        if not (y1 <= y2 < len(subtable[0])): return float("inf")

        min_R1 = min (subtable[x1 ][y1] , subtable[x1 ][ y2+1-2**ky ] )
        min_R2 = min (subtable[x2+1-2**kx][y1], subtable[x2+1-2**kx ][y2+1-2**ky])

        ret = min(min_R1, min_R2)

        return ret


### CODE HERE

def ans_one(A, C):
    N = len(A)
    M = len(A[0]
    )
    old_A = copy.deepcopy(A)
    A = copy.deepcopy(A)
    for i in range(N):
        for j in range(M):
            A[i][j] += C*(i + j)

    S = Sparse2(A)

    print(S._mat)

    ret = float("inf")
    for i in range(N):
        for j in range(M):
            candidate = old_A[i][j]
            candidate += min(
                S.query(i+1, j, N-1, M-1),
                S.query(i, j+1, N-1, M-1)
            ) - C*(i+j)
            ret = min(ret, candidate)
    return ret

def ans(A, C):
    ret = ans_one(A, C)
    A = [row[::-1] for row in A]
    ret = min(ret, ans_one(A, C))
    return ret

if False:
    import random
    H = 1000
    W = 1000
    A = [[random.randint(1, 100) for _ in range(W)] for _ in range(H)]

    Sparse2(A)
    # print(ans(A, 0))

else:
    H, W, C = read_int_tuple()
    A = []
    for _ in range(H):
        A += [read_int_list()]

    print(ans(A, C))