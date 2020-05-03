#!/usr/bin/env python3

BOUND = 1000

import random

x = str(random.randint(BOUND/5, BOUND))
y = str(random.randint(BOUND/5, BOUND))

m = ""
for i in range(BOUND):
	m += random.choice("NSEW")

print("1")
print(f"{x} {y} {m}")