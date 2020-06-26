#!/usr/bin/env pypy3

from sys import stdin, stdout
import array
 
def input():
    return stdin.readline().strip()

def ans(A, B):
    A = A[::-1]
    B = B[::-1]

    needs = [(A[i] - B[i], i) for i in range(len(A))]
    need, startIdx = sorted(needs)[-1]

    if sum(n[0] for n in needs) > 0:
        return "NO"

    if need <= 0:
        return "YES"

    while True:
        progressed = False
        for _ in range(len(A)):
            if need > 0:
                B[startIdx] = A[startIdx]
                progressed = True
            nextIdx = (startIdx + 1) % len(A)
            # print(f"{startIdx} -> {nextIdx} : {need}")
            # print(B)
            B[nextIdx] -= need
            if B[nextIdx] < 0:
                return "NO"
            need = max(0, A[nextIdx] - B[nextIdx])

            startIdx = nextIdx

        if need > 0: 
            return "NO"
        if need == 0:
            return "YES"
        if not progressed:
            return "NO"
        else:
            continue

    return "YES"



T = int(input())

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    B = input().split(' ')
    B = list(map(int, B))

    print(ans(A, B))
