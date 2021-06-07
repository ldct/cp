#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import product

class Matrix(list):
    MODULUS=998244353
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

### CODE HERE

H, W = read_int_tuple()

def grid_of_r1(row):
    ret = [[0]*H, [0]*H]
    for i,c in enumerate(row):
        if c == 'E': continue
        if c == 'O':
            if ret[0][i] == 1: return None
            ret[0][i] = 1
        if c == 'R':
            if ret[0][i] == 1: return None
            if i+1 >= H: return None
            if ret[0][i+1] == 1: return None
            ret[0][i] = 1
            ret[0][i+1] = 1
        if c == 'D':
            if ret[0][i] == 1: return None
            ret[0][i] = 1
            ret[1][i] = 1

    return ret

import copy

def grid_of_r2(start, row):
    ret = copy.deepcopy(start)
    for i,c in enumerate(row):
        if c == 'E': continue
        if c == 'O':
            if ret[1][i] == 1: return None
            ret[1][i] = 1
        if c == 'R':
            if ret[1][i] == 1: return None
            if i+1 >= H: return None
            if ret[1][i+1] == 1: return None
            ret[1][i] = 1
            ret[1][i+1] = 1

    return ret

mat = []
for _ in range((2**H)):
    mat += [[0]*(2**H)]

def bin_d(digits):
    ret = 0
    for i, d in enumerate(digits):
        ret += d*2**i
    return ret

for row1 in product('RDEO', repeat=H):
    grid1 = grid_of_r1(row1)
    if grid1 is not None:
        grid2 = grid_of_r2(grid1, 'OO')
        for row2 in product('REO', repeat=H):
            grid2 = grid_of_r2(grid1, row2)
            if grid2 is not None:
                a, b = grid2
                _a = bin_d(a)
                _b = bin_d(b)
                # print(_a, _b, row1, row2, grid2)
                mat[_a][_b] += 1

mat = Matrix(mat)
mat = mat**(W-1)
print(mat)