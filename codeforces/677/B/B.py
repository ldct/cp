#!/usr/bin/env pypy3

def ans(books):
    i = None
    j = None
    for k in range(len(books)):
        if books[k] == 0: continue
        j = k
        if i is None:
            i = k

    return sum(1-x for x in books[i:j+1])

for _ in range(int(input())):
    input()
    books = list(map(int, input().split()))
    print(ans(books))