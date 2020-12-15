#!/usr/bin/env pypy3

def ans(N, K):
    ret = list(range(1, N+1))
    for i in range(len(ret)):
        if i % 2 == 1:
            ret[i] = -ret[i]

    num_pos = len([r for r in ret if r > 0])

    lni = None
    for i in range(len(ret)):
        if ret[i] < 0:
            lni = i

    while K > num_pos:
        ret[lni] = -ret[lni]
        lni -= 2
        K -= 1

    lpi = None
    for i in range(len(ret)):
        if ret[i] > 0:
            lpi = i

    while K < num_pos:
        ret[lpi] = -ret[lpi]
        lpi -= 2
        K += 1
    print(*ret)

T = int(input())

for _ in range(T):
    N, K = input().split()
    N = int(N)
    K = int(K)

    ans(N, K)