#!/usr/bin/env pypy3


def guess(N):
    queries = []
    for i in range(1,N//4+1):
        queries += [2*i]
        queries += [2*(N//2+1-i)]
    if N//2 % 2 == 1:
        queries += [2*(N//2-N//4)]

    print(queries)

    print(f"? {queries[0]}", flush=True)
    input()

    noticed = dict()
    noticed[N] = True

    for i in range(1,len(queries)):
        print(f"? {queries[i]}", flush=True)
        diff = abs(queries[i] - queries[i-1])
        if "0" == input():
            noticed[diff] = False
            break
        else:
            noticed[diff] = True

    print(f"? 1", flush=True)
    if "1" == input():
        noticed[diff+1] = True
    if N%2 == 1:
        print(f"? {N}")
        if "1" == input():
            noticed[N-1] = True

    # print(noticed)
    for i in sorted(noticed.keys()):
        if noticed[i]:
            return i

T = int(input())

for _ in range(T):
    N = int(input())
    r = guess(N)
    print(f"= {r}", flush=True)