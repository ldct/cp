#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

### CODE HERE

class Query:
    def __init__(self, l, r, idx):
        self.l = l
        self.r = r
        self.idx = idx
        self.ans = None
    def __repr__(self):
        return f"({self.l}, {self.r}, {self.idx}, {self.ans})"

def update(idx, val, bit, n):
    while idx <= n:
        bit[idx] += val
        idx += idx & -idx

# querying the bit array
def bit_query(idx, bit, n):
    summ = 0
    while idx:
        summ += bit[idx]
        idx -= idx & -idx
    return summ

# tag: range frequency query
# tag:range-query
def answerQueries(arr, queries):
    queries.sort(key = lambda x: x.r)

    MAX = max(arr)+1
    n = len(arr)
    q = len(queries)

    bit = [0] * (n + 1)
    last_visit = [-1] * MAX

    query_counter = 0
    for i in range(n):
        if last_visit[arr[i]] != -1:
            update(last_visit[arr[i]] + 1, -1, bit, n)
        last_visit[arr[i]] = i
        update(i + 1, 1, bit, n)
        while query_counter < q and queries[query_counter].r == i:
            a = bit_query(queries[query_counter].r + 1, bit, n) - bit_query(queries[query_counter].l, bit, n)
            queries[query_counter].ans = a
            query_counter += 1

def ans(A):
    N = len(A) // 2

    indexes = []
    for _ in range(N+1):
        indexes += [[]]
    for i, a in enumerate(A):
        indexes[a] += [i]

    queries = []

    q = 0
    for i in range(1, N+1):
        l, r = indexes[i]
        if l > r: l, r = r, l
        l += 1
        r -= 1
        if not (l <= r): continue

        queries += [Query(l, r, q)]
        q += 1

    answerQueries(A, queries)

    swap = 0
    for query in queries:
        num_elems = query.r - query.l + 1 # s + 2r
        r = num_elems - query.ans
        s = query.ans - r
        swap += s

    return N + swap//2

N = read_int()
A = read_int_list()

print(ans(A))
