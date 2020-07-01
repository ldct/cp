#!/usr/bin/env pypy3

def ans(N, K):
    mat = []
    for _ in range(N):
        row = [0]*N
        mat += [row]

    offset = 0
    x = 0
    y = 0
    for i in range(K):
        mat[x][y] = 1
        x += 1
        y += 1
        x = x % N
        y = y % N
        
        if x == 0:
            y += 1
            assert(y <= N)

    R = []
    for i in range(N):
        R += [sum(mat[i])]
    
    mat = list(zip(*mat))

    C = []
    for i in range(N):
        C += [sum(mat[i])]

    # print val

    print((max(R) - min(R))**2 + (max(C) - min(C))**2)

    # print mat

    for row in mat:
        print(''.join(map(str,row)))


T = int(input())

for _ in range(T):
    n, k = input().split(' ')
    n = int(n)
    k = int(k)
    ans(n, k)