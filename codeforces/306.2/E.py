#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split(' ')))

def write_as_0(A):
    assert(len(A))

    if len(A) == 1:
        if A[0] == 0: return 0
        if A[0] == 1: return False

    if len(A) == 2:
        if A == [1, 0]:
            return (1, 0)
        else:
            return False

    if A[-1] == 1:
        return False

    left = write_as_1(A[:-1])
    if (left == False):
        return False
    else:
        return (left, 0)

def write_as_1(A):
    assert(len(A))

    if len(A) == 1:
        if A[0] == 1: return 0
        if A[0] == 0: return False

    if len(A) == 2:
        if A == [1, 0]:
            return False
        else:
            return tuple(A)

    if A[-1] == 1:
        return tuple(A)
    if A[-2] == 0:
        return (tuple(A[:-2]), (0, 0))

    # .....10

    i = len(A) - 2
    while i >= 0 and A[i] == 1:
        i-= 1
    if i == -1:
        return False

    left = tuple(A[:i])
    right = tuple(A[i+1:])

    # print(i, left, right)

    if len(left) == 0:
        return (0, right)
    else:
        return (left, (0, right))

def calculate(t):
    if t is False:
        return '-'
    if isinstance(t, int):
        return t
    t = tuple(map(calculate, t))
    if len(t) == 1:
        return calculate(t[0])
    if len(t) == 2:
        if t == (1, 0): return 0
        return 1
    else:
        a, b, *c = t
        return calculate([calculate([a, b]), calculate(c)])

def binary_sequences(length):
    if length == 0:
        return [[]]
    b = binary_sequences(length-1)
    b1 = map(lambda x: x+[1], b)
    b0 = map(lambda x: x+[0], b)
    return list(b0) + list(b1)

# for l in binary_sequences(5):
#     ans = write_as_0(l)
#     if ans is False:
#         print(l)
#     else:
#         assert calculate(ans) is 0

def to_impl(t):
    if isinstance(t, int):
        return str(t)
    else:
        t = map(to_impl, t)
        return '(' + '->'.join(t) + ')'

ans = write_as_0(A)
if ans is False:
    print("NO")
else:
    print("YES")
    print(to_impl(ans))