#!/usr/bin/env python3

def ans(A):
    i = 0
    j = len(A)-1

    ret = []

    for x in range(len(A)):
        if x % 2 == 0:
            ret += [A[i]]
            i += 1
        else:
            ret += [A[j]]
            j -= 1

    return ret

for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    print(*ans(A))