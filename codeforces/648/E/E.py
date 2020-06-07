#!/usr/bin/env python3

import random, itertools

def mix(elems):
    elems = ["{0:b}".format(e)[::-1] for e in elems]

    N = max(len(e) for e in elems)
    k = len(elems)

    for i in range(len(elems)):
        elems[i] = elems[i] + "0"*(N-len(elems[i]))

    ret = 0
    for i in range(N):
        ones = [e[i] for e in elems if e[i] == '1']
        if len(ones) >= max(1, k-2):
            ret += 2**i

    return ret

def slow_ans(arr):
    ret = 0
    for s in range(1, len(arr)+1):
        for ss in itertools.combinations(arr, s):
            if mix(ss) == 30:
                print(ss)
            ret = max(ret, mix(ss))
    return ret

def ans(arr):
    # greedy
    arr = sorted(arr)[::-1]
    ret = [arr[0]]

    for e in arr[1:]:
        if mix(ret + [e]) > mix(ret):
            ret += [e]

    return mix(ret)

print(ans([12, 16, 2, 5]), slow_ans([12, 16, 2, 5]))