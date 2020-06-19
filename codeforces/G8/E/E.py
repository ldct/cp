#!/usr/bin/env pypy3

from types import GeneratorType

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()


def ans(n, children):

    V = [-1]*(n+1)

    for i in range(1,n+1):
        if V[i] == -1:
            V[i] = 0
            for j in children[i]:
                V[j] = max(V[j], 1)
        elif V[i] == 0:
            assert(False)
        elif V[i] == 1:
            for j in children[i]:
                V[j] = max(V[j], 2)

    ret = []
    
    for i in range(1,n+1):
        if V[i] == 2:
            ret += [i]

    print(len(ret))
    print(' '.join(list(map(str, ret))))

T = int(input())

for _ in range(T):
    n, m = input().split(' ')
    n = int(n)
    m = int(m)

    children = dict()
    for i in range(1, n+1):
        children[i] = set()

    for _ in range(m):
        x, y = input().split(' ')
        x = int(x)
        y = int(y)

        children[x].add(y)

    ans(n, children)