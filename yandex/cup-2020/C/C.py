#!/usr/bin/env pypy3

from fractions import Fraction
from sys import stdin, stdout

def input():
    return stdin.readline().strip()

def solve(p,q,r,s):
    if p == r: return (None, None)
    a = Fraction(q-s, p-r)
    b = q - a*p
    return (a, b)

def ans1(A, B):
    pairs = set(zip(A, B))

    if len(pairs) == 0:
        return True

    if len(pairs) == 1:
        (x, y) = list(pairs)[0]
        return True

    pairs = list(pairs)

    p,q = pairs[0]
    r,s = pairs[1]

    a,b = solve(p,q,r,s)

    if a == None:
        return False

    if a == 0:
        return False

    newB = [a*x + b for x in A]

    if B == newB:
        return True

    return False

def ans(N1, N2, A, B):
    if N1 != N2: return "NO"

    A = sorted(A)
    B = sorted(B)
    if ans1(A,B) or ans1(A,B[::-1]):
        return "YES"
    return "NO"




for _ in range(int(input())):
    N1 = int(input())
    A = list(map(int, input().split()))
    N2 = int(input())
    B = list(map(int, input().split()))
    print(ans(N1, N2, A, B))
