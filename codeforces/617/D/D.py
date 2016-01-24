#!/usr/bin/env python3

x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()
x1, y1, x2, y2, x3, y3 = int(x1), int(y1), int(x2), int(y2), int(x3), int(y3)

def ans(p1, p2, p3):
	x1, y1 = p1
	x2, y2 = p2
	x3, y3 = p3
	# x,x    x
	# x  x   x
	if (x1 == x2 == x3): return 1

	#  x  x
	#  x
	if (x1, y1) == (x2, y3): 
		return 2

	if y1 == y2:
		if x1 < x3 < x2: 
			# x   x
			#   x  
			return 3
		if x2 < x3 < x1:
			return 3
		else:
			# 	  x x
			# x
			return 2

	return 3

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)

t1 = (y1, x1)
t2 = (y2, x2)
t3 = (y3, x3)
print(min(
	ans(p1, p2, p3),
	ans(p1, p3, p2),
	ans(p2, p1, p3),
	ans(p2, p3, p1),
	ans(p3, p1, p2),
	ans(p3, p2, p1),
	ans(t1, t2, t3),
	ans(t1, t3, t2),
	ans(t2, t1, t3),
	ans(t2, t3, t1),
	ans(t3, t1, t2),
	ans(t3, t2, t1)
))