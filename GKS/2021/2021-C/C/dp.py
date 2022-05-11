#!/usr/bin/env pypy3

from functools import lru_cache

def beats(a, b):
    if a == 'R': return b == 'S'
    if a == 'P': return b == 'R'
    if a == 'S': return b == 'P'

DRAW_REWARD = 0.1

@lru_cache(None)
def optimal(num_r, num_p, num_s, unassigned):
    if unassigned == 0:
        return (0.0, '')

    total = num_r + num_p + num_s
    if total == 0:
        weight_R = 1/3
        weight_P = 1/3
        weight_S = 1/3
    else:
        weight_R = num_s / total
        weight_P = num_r / total
        weight_S = num_p / total

    next_r = optimal(num_r+1, num_p, num_s, unassigned-1)
    throw_r = (weight_S + DRAW_REWARD*weight_R + next_r[0], 'R'+next_r[1])

    next_p = optimal(num_r, num_p+1, num_s, unassigned-1)
    throw_p = (weight_R + DRAW_REWARD*weight_P + next_p[0], 'P'+next_p[1])

    s = optimal(num_r, num_p, num_s+1, unassigned-1)
    throw_s = (weight_P + DRAW_REWARD*weight_S + s[0], 'S'+s[1])

    return max([throw_r, throw_p, throw_s])

print(optimal(0, 0, 0, 60))