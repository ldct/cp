#!/usr/bin/env pypy3

import random
for _ in range(100):
	testcase = [random.randint(1,100) for _ in range(100)]
	print(100)
	print(*testcase)
