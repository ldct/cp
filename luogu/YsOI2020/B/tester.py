#!/usr/bin/env python3

import random

N = random.randint(100, 200)
Q = 20

print(N, Q)

test_case = [random.randint(1,100) for _ in range(N)]
print(*test_case)

for _ in range(Q):
    query_type = random.choice("123")

    l = random.randint(1, N)
    r = random.randint(l, N)

    if query_type == "1":
        x = random.randint(1,100)
        print(f"1 {l} {r} {x}")
    elif query_type == "2":
        y = random.randint(1,N)
        print(f"2 {l} {r} {y}")
    else:
        z = random.randint(1,N)
        print(f"3 {z}")