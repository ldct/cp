#!/usr/bin/env pypy

from __future__ import division, print_function

import itertools, sys, math

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

MODULUS = 10**9+7

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import product

class UnionFind:
    def __init__(self, R, C):
        self.parent = dict()
        for r in range(R):
            for c in range(C):
                self.parent[(r, c)] = (r, c)

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def join(self, a, b):
        self.parent[self.find(b)] = self.find(a)

def ans(R, C, mat):
    uf = UnionFind(R, C)

    for x in range(R):
        for y in range(C):
            if mat[x][y] == '#': continue
            if x == 0 or mat[x-1][y] == '#':
                xx = x+1
                while xx < R and mat[xx][y] != '#':
                    xx += 1
                xx -= 1
                if xx - x + 1 > 1:
                    for t in range(xx-x+1):
                        uf.join((x + t, y), (xx - t, y))
            if y == 0 or mat[x][y-1] == '#':
                yy = y+1
                while yy < C and mat[x][yy] != '#':
                    yy += 1
                yy -= 1
                if yy - y + 1 > 1:
                    for t in range(yy-y+1):
                        uf.join((x, y+t), (x, yy-t))

    char_of_leader = dict()

    for x in range(R):
        for y in range(C):
            if mat[x][y] not in "#.":
                char_of_leader[uf.find((x, y))] = mat[x][y]

    ret = 0

    for x in range(R):
        for y in range(C):
            leader = uf.find((x, y))
            if leader in char_of_leader:
                if mat[x][y] == ".": ret += 1
                mat[x][y] = char_of_leader[leader]


    return ret, mat

for t in range(read_int()):
    mat = []
    R, C = read_int_tuple()
    for _ in range(R):
        mat += [list(input())]

    a, b = ans(R, C, mat)
    print("Case #" + str(t+1) + ": " + str(a))
    for row in b:
        print(''.join(row))
