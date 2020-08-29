#!/usr/bin/env pypy3

from collections import Counter

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def bootstrap(f, stack=[]):
    from collections import defaultdict
    from types import GeneratorType

    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

@bootstrap
def ans_seg(A):	
	if len(A) == 0: yield 0

	option1 = len(A)
	
	m = min(A)

	for i in range(len(A)):
		A[i] -= m

	option2 = m + (yield ans(A))

	yield min(option1, option2)

@bootstrap
def ans(A):

	last_seg = []
	segs = []

	for a in A:
		if a == 0:
			segs += [last_seg]
			last_seg = []
		else:
			last_seg += [a]

	if len(last_seg):
		segs += [last_seg]

	ret = 0
	for seg in segs:
		ret += yield ans_seg(seg)
	yield ret

N = int(input())
S = list(map(int, input().split()))

print(ans(S))

# test_case = [i for i in range(1,5000)]
# print(ans(test_case))
