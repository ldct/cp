#!/usr/bin/env pypy3

def ans(K):
    ret = []
    for _ in range(8):
        ret += [['X']*8]

    assert(1 <= K <= 64)


    for i in range(8):
        for j in range(8):
            if K > 0:
                ret[i][j] = '.'
                K -= 1

    ret[0][0] = 'O'


    for row in ret:
        print(''.join(row))
    print()

T = int(input())

for _ in range(T):
    K = int(input())
    ans(K)