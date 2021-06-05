#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from collections import defaultdict

def ans(S):
    counter = defaultdict(int)

    j = 0
    counter[S[0]] += 1
    ret = 0
    for i in range(len(S)):
        # print("start", i, j, counter)
        while j < i:
            j += 1
            counter[S[j]] += 1
        # print("caught up", i, j, counter)

        if not ok(counter):
            counter[S[i]] -= 1
            continue

        while j+1 < len(S) and S[j+1] in 'ha':
            j += 1
        # print(i, j, counter)
        ret = max(ret, j-i+1)
        counter[S[i]] -= 1

    return ret

def ans_ac(laugh):
    x=0
    y=0
    prev='z'
    for i in laugh:
        if( i =="a"or i=="h"):
            if i!=prev:
                x+=1
            else:
                x=1
            prev=i
        else:
            prev='z'
            x=0
        if x>y:
            y=x
    return y


def ans_slow(S):
    def ok(S):
        for c in S:
            if c not in 'ha': return False
        return True

    ret = 0
    for i in range(len(S)+1):
        for j in range(i+1, len(S)+1):
            assert(j-i == len(S[i:j]))
            if ok(S[i:j]):
                ret = max(ret, j-i)
    return ret

if True:
    tc = 'aahha'
    print(ans_slow(tc))
    print(ans_ac(tc))
elif True:
    import random
    for _ in range(1000000):
        tc = ''.join(random.choice('abh') for _ in range(5))
        print(tc)
        assert(ans_ac(tc) == ans_slow(tc))
else:
    N = read_int()
    S = input()[0:N]
    print(ans(S))