#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, Q = read_int_tuple()
A = read_int_list()
original_queries = []
for _ in range(Q):
    original_queries += [read_int()-1]

sorted_queries = sorted(original_queries)
sorted_answers = []
answers_dict = dict()
q = 0
passed = 0

A = [0] + A + [A[-1]+10**20]
for i in range(len(A)-1):
    low = A[i]+1
    high = A[i+1]-1
    if not low <= high: continue

    while q < len(sorted_queries) and (passed <= sorted_queries[q] <= passed + (high - low)):
        # print("can answer", sorted_queries[q], )
        sorted_answers += [sorted_queries[q] - passed + low]
        q += 1

    # print(list(range(low, high+1)))

    passed += (high - low + 1)

for q, a in zip(sorted_queries, sorted_answers):
    answers_dict[q] = a

for q in original_queries:
    print(answers_dict[q])
