#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import math, copy, random

class Sparse1:
    def __init__(self, arr):
        self._arr = arr[:]

        N = len(arr)
        self.table = [arr[:]]

        for j in range(1, 1+math.floor(math.log(N, 2))):
            self.table += [[-1]*N]
            assert(0 <= j < len(self.table))
            for i in range(N-2**(j-1)):
                self.table[j][i] = min(self.table[j-1][i], self.table[j-1][i+2**(j-1)])

    def check(self):
        for i in range(len(self._arr)):
            for j in range(i, len(self._arr)):
                self.query(i, j)

    def query(self, x, y):
        gap = y-x+1
        k = math.floor(math.log(gap,2))
        ret = min(self.table[k][x],self.table[k][y+1-2**k])
        assert(ret == min(self.table[0][x:y+1]))
        return ret

if False:
    for N in range(1, 33):
        for _ in range(100):
            arr = [random.randint(1, 10) for _ in range(N)]
            s = Sparse1(arr)
            s.check()
        print("checked", N)

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
                row += [copy.deepcopy(mat)]
                if (i, j) != (0, 0):
                    for x in range(N):
                        for y in range(M):
                            row[-1][x][y] = -1
            self.table += [row]

        for ir in range(N):
            for jc in range(1, lM):
                for ic in range(M-2**(jc-1)):
                    self.table[0][jc][ir][ic]=min(self.table[0][jc-1][ir][ic],self.table[0][jc-1][ir][ic+2**(jc-1)])

        for jr in range(1, lN):
            for ir in range(N-2**(jr-1)):
                for jc in range(lM):
                    for ic in range(M):
                        self.table[jr ][jc ][ir][ic ] = min(self.table[jr-1 ][jc ][ir][ic ],self.table[jr-1 ][jc][ir+2**(jr-1) ][ic ])

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
        lenx=x2-x1+1
        kx=math.floor(math.log(lenx))
        leny=y2-y1+1
        ky=math.floor(math.log(leny))

        min_R1 = min ( self.table[kx ][ky][x1 ][y1 ] , self.table[kx ][ky][x1 ][ y2+1-2**ky ] )
        min_R2 = min ( self.table[kx ][ky][x2+1-2**kx ][y1 ], self.table[kx ][ky][x2+1-2**kx ][y2+1-2**ky ] )

        ret = min(min_R1, min_R2)

        assert(ret == self.query_slow(x1, y1, x2, y2))

        return ret

mat = [[3, 8, 1, 5, 7]]
# mat = [[random.randint(1, 10) for _ in range(5)]]
s = Sparse2(mat)
t = s.table
for i in range(len(t)):
    for j in range(len(t[i])):
        print(t[i][j])
s.check()

for _ in range(0):
    mat = [[random.randint(1, 2) for _ in range(8)] for _ in range(8)]
    s = Sparse2(mat)
    s.check()
    print(s.table)




# ### CODE HERE

# for _ in range(read_int()):
#     pass