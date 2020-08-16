#!/usr/bin/env python3

input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)
C = sorted(C)

ret = 0

a = len(A)-1
b = len(B)-1
c = len(C)-1

ret = 0

while True:
    if a < 0:
        aa = 0
    else:
        aa = A[a]

    if b < 0:
        bb = 0
    else:
        bb = B[b]

    if c < 0:
        cc = 0
    else:
        cc = C[c]

    this_max = max(aa*bb, bb*cc, aa*cc)

    if this_max == 0:
        break

    if aa*bb == this_max:
        a -= 1
        b -= 1
    elif aa*cc == this_max:
        a -= 1
        c -= 1
    elif bb*cc == this_max:
        b -= 1
        c -= 1
    else:
        assert(False)

    ret += this_max

print(ret)