#!/usr/bin/env python3

def decreasing_partitions(x, width):
    if x <= 0:
        yield []
        return
    if x == 0:
        yield [0]
        return
    for w in range(1, max(x, width + 1)):
        for dp in decreasing_partitions(x - w, w):
            yield [w] + dp

for t in range(int(input(''))):
    (N, M, K) = input('').split(' ')
    N = int(N)
    M = int(M)
    K = int(K)

    print(list(decreasing_partitions(5, 5)))

    print("Case #%i: %i %i %i" % (t + 1, N, M, K))