#!/usr/bin/env python3

N, M = input().split(' ')
N, M = int(N), int(M)
L = input().split(' ')
L = list(int(x) for x in L)

def answer(N, M, L):
    offsets = [0]
    for i in range(M-1):
        offsets += [1]

    overhang = 0
    for ii in range(M-1):
        # we are considering the ith object, counting from 0
        i = M-1-ii
        left_edge = i+1
        right_edge = left_edge + L[i] - 1 + overhang

        if right_edge > N:
            return "-1"

        max_right_edge = right_edge + L[i-1] - 1
        if max_right_edge > N:
            max_right_edge = N

        offsets[i] += (max_right_edge - right_edge)
        parent_right_edge = i + L[i-1] - 1
        overhang = max(0, max_right_edge - parent_right_edge)

    if L[0] + overhang < N:
        return "-1"

    pos = 1
    ret = [1]
    for o in offsets[1:]:
        pos += o
        ret += [pos]

    return ' '.join(str(r) for r in ret)

print(answer(N, M, L))