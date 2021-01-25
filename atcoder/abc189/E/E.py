#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

class Matrix(list):
    def __matmul__(self, B) :
        A = self
        return Matrix([[sum(A[i][k]*B[k][j] for k in range(len(B)))
                    for j in range(len(B[0])) ] for i in range(len(A))])


    def vecmul(self, v):
        vv = []
        for c in v:
            vv += [[c]]
        return (self @ vv)

    @classmethod
    def Identity(cls, size):
        size = range(size)
        return Matrix([[(i==j)*1 for i in size] for j in size])

### CODE HERE

mat1 = Matrix([
    [0, 1, 0],
    [-1, 0, 0],
    [0, 0, 1],
])

mat2 = Matrix([
    [0, -1, 0],
    [1, 0, 0],
    [0, 0, 1],
])

def translate(x, y):
    return Matrix([
        [1, 0, x],
        [0, 1, y],
        [0, 0, 1],
    ])

pure_flipx = Matrix([
    [-1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
])

pure_flipy = Matrix([
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 1],
])

def flipx(p):
    return translate(p, 0) @ pure_flipx @ translate(-p, 0)

def flipy(p):
    return translate(0, p) @ pure_flipy @ translate(0, -p)

t = Matrix.Identity(3)

points = []
for _ in range(read_int()):
    (x, y) = read_int_tuple()
    points += [(x, y, 1)]

transforms = [Matrix.Identity(3)]

for _ in range(read_int()):
    op = read_int_list()

    if op[0] == 1:
        t = mat1
    elif op[0] == 2:
        t = mat2
    elif op[0] == 3:
        t = flipx(op[1])
    elif op[0] == 4:
        t = flipy(op[1])
    else:
        assert(False)

    transforms += [t @ transforms[-1]]

# print(transforms)

for _ in range(read_int()):
    A, B = read_int_tuple()
    [[x], [y], _] = transforms[A].vecmul(points[B-1])
    print(x, y)
