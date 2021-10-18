#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N, A, t):
    if N == 3:
        print("Case #" + str(t+1) + ": POSSIBLE")
        print(0, 0)
        print(0, 1)
        print(0, A)
    elif N == 4:
        if A == 1:
            print("Case #" + str(t+1) + ": IMPOSSIBLE")
        else:
            a = A-1
            b = 1
            print("Case #" + str(t+1) + ": POSSIBLE")
            print(0, 0)
            print(1, 0)
            print(1, b)
            print(0, a)
    elif N == 5:
        if A <= 3:
            print("Case #" + str(t+1) + ": IMPOSSIBLE")
        else:
            for b in range(A):
                a = A - 2*b
                if a != b and b > 0 and a > 0: break

            print("Case #" + str(t+1) + ": POSSIBLE")
            print(0, 0)
            print(0, a)
            print(1, b)
            print(2, b)
            print(1, 0)


T = int(input())
for t in range(T):
    N, A = read_int_tuple()
    ans(N, A, t)
