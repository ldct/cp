#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE


def dump(lst):
    lst = [l+1 for l in lst]
    lst = [len(lst)] + lst
    print(*lst)

def ans(A):
    A = [a % 200 for a in A]

    def exclude(lst):
        for i in range(len(A)):
            if i not in lst: return i
        assert(False)
    way_to_make = {0: []}
    for i,a in enumerate(A):
        nw = dict(way_to_make)
        for w in way_to_make:
            if (w+a)%200 in way_to_make:
                if way_to_make[(w+a)%200] == []:
                    nw[(w+a)%200] = nw[w] + [i]
                else:
                    return((way_to_make[(w+a)%200]), way_to_make[w] + [i])
            else:
                nw[(w+a)%200] = nw[w] + [i]
        way_to_make = nw
    if 0 < len(way_to_make[0]) < len(A):
        return (way_to_make[0], way_to_make[0] + [exclude(way_to_make[0])])
    return False

def ans_slow(A):
    from itertools import combinations
    def sub_lists(my_list):
        subs = []
        for i in range(0, len(my_list)+1):
            temp = [list(x) for x in combinations(my_list, i)]
            if len(temp)>0:
                subs.extend(temp)
        return subs

    SL = sub_lists(A)[1:]
    for i in range(len(SL)):
        for j in range(i+1, len(SL)):
            if sum(SL[i])%200 == sum(SL[j])%200:
                return True
    return False

if False:
    print(ans([99, 101, 1]))
elif False:
    import random
    for _ in range(1000000):
        A = [random.randint(1, 200) for _ in range(4)]
        if ans(A) != ans_slow(A):
            print(A, ans(A), ans_slow(A))
            assert(False)
else:
    input()
    A = read_int_list()

    r = ans(A)
    if r == False:
        print("No")
    else:
        (p, q) = r
        print("Yes")
        dump(p)
        dump(q)