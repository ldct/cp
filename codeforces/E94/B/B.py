#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(p, f, cs, cw, s, w):
	assert(s <= w) # swords are lighter

	def ok(n):
		ns = 0
		nw = 0

		if n <= cs:
			ns = n
			nw = 0
		else:
			ns = cs
			nw = n - cs

		if not (0 <= ns <= cs): return False
		if not (0 <= nw <= cw): return False

		for ps in range(0, ns+1):
			fs = ns - ps
			
			p_cap = p - ps*s
			f_cap = f - fs*s

			if p_cap < 0 or f_cap < 0: continue

			pw = p_cap // w
			fw = f_cap // w

			if pw + fw >= nw: return True
		
		return False

	low = 0
	high = 5*10**5+10

	assert(ok(low))
	assert(not ok(high))

	while high - low > 5:
		mid = (low + high) // 2
		if ok(mid):
			low = mid
		else:
			high = mid

	for i in range(low, high+1):
		if not ok(i):
			return i-1


def ans2(p, f, cs, cw, s, w):
	if s > w:
		return ans(p, f, cw, cs, w, s)
	return ans(p, f, cs, cw, s, w)

T = int(input())
for t in range(T):
	p, f = input().split()
	cs, cw = input().split()
	s, w = input().split()
	print(ans2(int(p), int(f), int(cs), int(cw), int(s), int(w)))
