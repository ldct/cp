#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans2(N):
    ret = 0
    for a in range(1, 10+int(N**(1/2))):
        if N % a != 0: continue
        b = N // a
        if a*b <= N:
            ret += 1
    print("ans2", N, ret)
    return ret

def ans_slow(N):
    ret = set()
    for a in range(1, N+1):
        for b in range(a, N+1):
            for c in range(1, N+1):
                if not (a <= b <= c): continue
                if a*b*c <= N:
                    ret.add((a, b, c))
    return len(ret)

def ans(N):
    ret = 0
    for a in range(1, 2+int(N**(1/3))):
        bc = N // a
        for b in range(a, 2+int(bc**(1/2))):
            if a*b*b > N: continue

            c_low = b
            assert(a*b*c_low <= N)

            c_high = N // (a*b) - 2
            while a*b*c_high <= N: c_high += 1

            ret += (c_high - c_low)
    return ret

# for N in range(1, 1000):
#     a_s = ans_slow(N)
#     a = ans(N)
#     assert(a == a_s)
#     if N % 10 == 0: print("ok", N)

# print("ok")

print([ans(i) for i in range(1, 20)])
# print(ans(read_int()))