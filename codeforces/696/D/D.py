#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans_strict(A):

    if len(A) == 2: return A[0] == A[1]

    used = True
    A = A[:]
    i = 1
    while True:
        if i == len(A): return A[-1] == 0

        if A[i] >= A[i-1]:
            A[i] -= A[i-1]
            i += 1
        else:
            if used: return False
            if i+1 == len(A): return False
            A[i], A[i+1] = A[i+1], A[i]
            used = True

def ans_slow(A):
    if ans_strict(A): return True
    for i in range(len(A)-1):
        new_A = A[:]
        new_A[i], new_A[i+1] = new_A[i+1], new_A[i]
        if ans_strict(new_A): return True
    return False

def ans_one_pass(A):

    A = A[:]
    for i in range(1, len(A)):
        A[i] -= A[i-1]

    return A

def ok(op):
    for c in op:
        if c < 0: return False
    return op[-1] == 0

def ans(A):
    if len(A) == 2: return A[0] == A[1]

    op = ans_one_pass(A)

    print(op)

    if ok(op): return True

    for i in range(0, len(A)-1):
        d = A[i+1] - A[i]
        if i % 2 == 0: d *= -1

        if i < 0 and min(op[0:i]) < 0: continue
        if op[i] - d < 0: continue
        if op[i+1] + 2*d < 0: continue
        if len(op[i+2::2]) and min(op[i+2::2]) + 2*d < 0: continue
        if len(op[i+3::2]) and min(op[i+3::2]) - 2*d < 0: continue

        # if len(op) % 2 == 0:
        #     if op[-1] + 2*d != 0: continue
        # else:
        #     if op[-1] - 2*d != 0: continue

        return True
    return False

if False:
    tc = [2, 2, 2, 1, 3]
    print(ans(tc))

elif False:
    import random
    for _ in range(100):
        n = 3
        tc = [random.randint(1, 5) for _ in range(n)]
        print(tc, ans_slow(tc), ans(tc))

else:
    for _ in range(read_int()):
        input()
        A = read_int_list()
        if ans(A) == True:
            print("YES")
        elif ans(A) == '?':
            print('?')
        else:
            print("NO")
