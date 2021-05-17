#!/usr/bin/env python3

import collections
from itertools import chain, combinations

T = int(input(''))

def xsum(arr):
    xsum_of_position = []
    for l in range(len(arr[0])):
        sum = 0
        for n in arr:
            sum += int(n[l])
        xsum_of_position += [sum]
    return xsum_of_position

def flip_bit(str, i):
    sa = list(str)
    if sa[i] == '0':
        sa[i] = '1'
    else:
        sa[i] = '0'
    return ''.join(sa)

def flip_all_bits(str_arr, i):
    return list(map(lambda str: flip_bit(str, i), str_arr))

def do_all_flips(str_arr, i_arr):
    for i in i_arr:
        str_arr = flip_all_bits(str_arr, i)
    return str_arr

def is_same_set(s1, s2):
    return collections.Counter(s1) == collections.Counter(s2)

def powerset(iterable): #python docs
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def handle_trap(device, outlet, traps):
    for combi in powerset(traps):
        if is_same_set(device, do_all_flips(outlet, combi)):
            return str(len(combi))
    return "NOT POSSIBLE"
    
for i in range(T):
    first_line = input('').split(' ')
    N = int(first_line[0])
    L = int(first_line[1])

    outlet = input('').split(' ')
    device = input('').split(' ')
    
    x_o = xsum(outlet)
    x_d = xsum(device)
    x_diff = []

    for l in range(L):
        x_diff += [x_o[l] - x_d[l]]

    if (sum(x_diff) > 0 and N % 2 == 0):
        print("Case #%d: NOT POSSIBLE" % (i + 1))
    elif (N % 2 == 0):
        no_flips = 0
        traps = []
        for l in range(L):
            if abs(x_diff[l]) == N/2:
                traps += [l]
            elif x_diff[l] != 0:
                no_flips += 1
                outlet = flip_all_bits(outlet, l)
        if len(traps):
            print("Case #%d: %s" % (i + 1, handle_trap(device, outlet, traps)))      
        elif (is_same_set(device, outlet)):
            print("Case #%d: %d" % (i + 1, no_flips))
        else:
            print("Case #%d: NOT POSSIBLE" % (i + 1))
    else:
        no_flips = 0
        for l in range(L):
            if x_diff[l] != 0:
                no_flips += 1
                outlet = flip_all_bits(outlet, l)
        if (is_same_set(device, outlet)):
            print("Case #%d: %d" % (i + 1, no_flips))
        else:
            print("Case #%d: NOT POSSIBLE" % (i + 1))