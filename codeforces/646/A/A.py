#!/usr/bin/env python3

T = int(input())

def ans(A, x):

    pos_odd = []
    pos_even = []
    ret = []

    for i, e in enumerate(A):
        if e % 2 == 1:
            pos_odd += [i]
        else:
            pos_even += [i]
    
    if len(pos_odd) == 0:
        return None

    # grab an odd number
    ret += [pos_odd[0]]
    pos_odd = pos_odd[1:]
    x -= 1

    assert(len(pos_even) >= 0)
    assert(len(pos_odd) >= 0)
    
    # now select x numbers with an even sum

    # greedily use all pairs of odd numbers
    if len(pos_odd) % 2 == 1:
        pos_odd = pos_odd[1:]

    while x > 1 and len(pos_odd):
        x -= 2
        ret += pos_odd[0:2]
        pos_odd = pos_odd[2:]

    assert(x >= 0)

    while x > 0 and len(pos_even):
        x -= 1
        ret += pos_even[0:1]
        pos_even = pos_even[1:]

    if x == 0:
        return ret

    return None

def ans2(A, x):
    ret = ans(A, x)
    if ret is None:
        return "No"

    if ret == "Yes":
        return "Yes"

    assert(len(ret) == x)
    sum = 0
    for i in ret:
        sum += A[i]
    assert(sum % 2 == 1)


    return "Yes"

for t in range(T):
    n, x = input().split(' ')
    n = int(n)
    x = int(x)

    A = input().split(' ')
    A = [int(a) for a in A]

    print(ans2(A, x))