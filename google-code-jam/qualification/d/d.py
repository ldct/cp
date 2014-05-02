#!/usr/bin/env python3

T = int(input(''))

def count_nk(ranking):
    unmatched_n = 0
    nk = 0
    for (_, player) in reversed(ranking):
        if player == 'naomi':
            unmatched_n += 1
        else:
            if unmatched_n > 0:
                unmatched_n -= 1
                nk += 1
    return nk

def count_kn(ranking):
    unmatched_k = 0
    kn = 0
    for (_, player) in reversed(ranking):
        if player == 'ken':
            unmatched_k += 1
        else:
            if unmatched_k > 0:
                unmatched_k -= 1
                kn += 1
    return kn

for i in range(T):
    N = int(input(''))
    naomi = input('').split(' ')
    ken = input('').split(' ')

    naomi = [(float(x), 'naomi') for x in naomi]
    ken = [(float(x), 'ken') for x in ken]
    
    ranking = sorted(ken + naomi)

    print("Case #%d:" % (i + 1), count_nk(ranking), N - count_kn(ranking))