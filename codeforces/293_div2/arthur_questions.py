#!/usr/bin/env python3

import sys, math

N, K = input().split(' ')
N = int(N)
K = int(K)

raw_a = input().split(' ')
a = ['?'] * N
known_idxs = set()

# if (N, K) == (99941, 52):
#     print(' '.join(raw_a[500:600]))

for i, e in enumerate(raw_a):
    if e != '?':
        a[i] = int(e)
        known_idxs.add(i)

def fail():
    print('Incorrect sequence')
    sys.exit(0)

def do_fix(aa, b, c, d, e, f = 1):
    assert(len(range(aa, b, c)) == len(range(d, e, f)))
    a[aa:b:c] = range(d, e, f)

def fix(start, end):

    # fix [start...end] with stride K

    # print(a[start:end+1:K])

    l = len(range(start, end+1, K))

    if l == 2 and a[start] == '?' and a[end] == '?':
        a[start] = 0
        a[end] = 1
        return

    a_e = float('+inf') if a[end] == '?' else a[end]
    a_s = float('-inf') if a[start] == '?' else a[start]

    left_0 = l - a_e - 2
    right_0 = -1 - a_s

    if (left_0 > right_0):
        fail()
    else:
        assert(left_0 <= right_0)

        L = l + (a[start] == '?') + (a[end] == '?')
        opt_0 = (L - 2) // 2 - (a[start] == '?')

        opt_0 = min(opt_0, right_0)
        opt_0 = max(opt_0, left_0)

        s = -opt_0
        do_fix(start+K, end, K, s, s+l-2)

    # print("done middle", a[start:end+1:K])

    if a[end] == '?' and end-K >= 0:
        a[end] = max(0, a[end-K] + 1)
    elif a[end] == '?':
        a[end] = 0

    # print(":)", a[start:end+1:K])

    if a[start] == '?' and start+K < N:
        a[start] = min(0, a[start+K] - 1)
    elif a[start] == '?':
        a[start] = 0

    # print("done", a[start:end+1:K])

for s in range(0, K):
    sub_idxs = list(range(s, N, K))

    sub_ki = [i for i in sub_idxs if i in known_idxs]
    if sub_idxs[0] not in sub_ki:
        sub_ki = [sub_idxs[0]] + sub_ki
    if sub_idxs[-1] not in sub_ki:
        sub_ki = sub_ki + [sub_idxs[-1]]

    if len(sub_ki) == 1:
        (i, ) = sub_ki
        if a[i] == '?':
            a[i] = 0

    for i in range(0, len(sub_ki) - 1):
        fix(sub_ki[i], sub_ki[i + 1])

print(' '.join(map(str, a)))