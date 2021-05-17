#!/usr/bin/env python3

def xor_str(a, b):
    return "{0:b}".format(int(a, 2) ^ int(b, 2))

def lmap(a, b):
    return list(map(a, b))

def get_ints():
    return map(int, input('').split(' '))

for t in range(int(input(''))):
    (N, L) = get_ints()

    outlet = input('').split(' ')
    device = input('').split(' ')

    xor_table = [[None] * N for i in range(N)]
    for i, o in enumerate(outlet):
        for j, d in enumerate(device):
            xor_table[i][j] = xor_str(o, d)

    sets = lmap(set, zip(*xor_table)) + lmap(set, xor_table)
    valids = set.intersection(*sets)

    if (len(valids) == 0):
        print("Case #%d: NOT POSSIBLE" % (t+1))
    else:
        def sum_ones(s):
            return sum(map(int, s))
        min_flips = min(map(sum_ones, valids))
        print("Case #%d: %d" % (t+1, min_flips))