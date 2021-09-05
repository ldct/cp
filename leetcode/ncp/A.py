#!/usr/bin/env pypy3

import math, itertools

def ln(x):
    return math.log(x, math.e)

def ncp(arr):
    ret = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if math.gcd(arr[i], arr[j]) == 1:
                ret += 1
    return ret

def valid_ncps(n):
    rep = dict()
    ret = set()
    P = 3
    for ss in itertools.product(range(P+1), repeat=n):
        res = ncp(ss)
        if res not in rep:
            rep[res] = ss
        else:
            rep[res] = min(rep[res], ss)
        ret.add(ncp(ss))

    return rep


r = valid_ncps(5)
for k in sorted(r.keys()):
    print(k, r[k])
