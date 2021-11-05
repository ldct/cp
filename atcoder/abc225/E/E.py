#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

"""
About 2x as fast as Fraction; does not do reduction
"""
class FastFraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __eq__(self, other):
        return self.top * other.bottom == self.bottom * other.top

    def __lt__(self, other):
        if self == other: return False
        if other.bottom == 0: return True
        return self.top*other.bottom < self.bottom*other.top

    def asfloat(self):
        return self.top / self.bottom

    def __ge__(self, other):
        return not (self < other)

Fraction = FastFraction

intervals = []

def f(p):
    x, y = p
    return Fraction(y, x)

for _ in range(read_int()):
    x, y = read_int_list()
    a = (x-1, y)
    b = (x, y-1)

    intervals += [(f(b), f(a))]

def ans(intervals):
    ret = 0
    intervals.sort(lambda p : p[1])
    rightmost = Fraction(-1, 1)
    for a, b in intervals:
        if a >= rightmost:
            ret += 1
            # print("pick", a, b)
            rightmost = b

    return ret

print(ans(intervals))